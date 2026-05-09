#NAME  :ENOCK KIBET
REG NO :CIT-227-068/2024

# Task 2(a): Australia Map Coloring
def is_valid(region, color, assignment, adjacency):
    """Check if the color assignment is consistent with neighbors."""
    for neighbor in adjacency.get(region, []):
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack_coloring(regions, colors, assignment, adjacency):
    """Backtracking algorithm to find a valid coloring."""
    if len(assignment) == len(regions):
        return assignment

    # Select the next unassigned region
    unassigned = [r for r in regions if r not in assignment]
    region = unassigned[0]

    for color in colors:
        if is_valid(region, color, assignment, adjacency):
            assignment[region] = color
            result = backtrack_coloring(regions, colors, assignment, adjacency)
            if result:
                return result
            # Backtrack
            del assignment[region]
    return None

# Define Australia Data
regions_au = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
colors_au = ['Red', 'Green', 'Blue']
adjacency_au = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q':  ['NT', 'SA', 'NSW'],
    'NSW': ['Q', 'SA', 'V'],
    'V':  ['SA', 'NSW'],
    'T':  []  # Tasmania has no land borders
}

solution_au = backtrack_coloring(regions_au, colors_au, {}, adjacency_au)
print("Australia Coloring Solution:", solution_au)
