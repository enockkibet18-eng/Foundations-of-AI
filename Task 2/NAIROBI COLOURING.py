NAME  :ENOCK KIBET
REG NO:CIT-227-068/2024
UNIT  :FOUNDATION OF AI

# Task 2(b): Nairobi Sub-Counties (Simulative Map)
def greedy_coloring(sub_counties, adjacency):
    # Sort sub-counties by number of neighbors (Highest degree first) to optimize
    nodes = sorted(sub_counties, key=lambda x: len(adjacency.get(x, [])), reverse=True)
    result = {}

    for node in nodes:
        # Check colors of neighbors
        neighbor_colors = {result[neighbor] for neighbor in adjacency.get(node, []) if neighbor in result}
        
        # Assign the first available color (represented by integers 0, 1, 2...)
        color = 0
        while color in neighbor_colors:
            color += 1
        result[node] = color
    
    return result

# 17 Nairobi Sub-Counties (Simulative adjacency list)
nairobi_sub_counties = [
    "Westlands", "Dagoretti North", "Dagoretti South", "Langata", "Kibra", 
    "Roysambu", "Kasarani", "Ruaraka", "Embakasi South", "Embakasi North", 
    "Embakasi Central", "Embakasi East", "Embakasi West", "Makadara", 
    "Kamkunji", "Starehe", "Mathare"
]

# Simulative adjacency (simplified for demonstration)
nairobi_adj = {
    "Westlands": ["Dagoretti North", "Starehe", "Roysambu"],
    "Dagoretti North": ["Westlands", "Dagoretti South", "Kibra"],
    "Kibra": ["Dagoretti North", "Langata", "Starehe"],
    "Starehe": ["Westlands", "Mathare", "Kamkunji", "Kibra"],
    "Mathare": ["Starehe", "Ruaraka", "Kamkunji"],
    # ... (remaining adjacencies follow similar logic)
}

# Run coloring
coloring_result = greedy_coloring(nairobi_sub_counties, nairobi_adj)
num_colors = max(coloring_result.values()) + 1

print(f"Nairobi Coloring complete using {num_colors} colors.")
for county, color_id in coloring_result.items():
    print(f"{county}: Color {color_id}")
