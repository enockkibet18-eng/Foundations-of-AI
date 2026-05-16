#Enock Kibet
#CIT-227=068/2024

# task4.py - BFS and DFS from start to goal
# Uses a simple graph, prints the path found

from collections import deque

# The graph I'm using for testing
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# BFS using a queue
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set([start])

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == goal:
            return path

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
    return None

# DFS using recursion
def dfs(graph, start, goal, visited=None, path=None):
    if visited is None:
        visited = set()
    if path is None:
        path = [start]

    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph[start]:
        if neighbor not in visited:
            result = dfs(graph, neighbor, goal, visited, path + [neighbor])
            if result:
                return result
    return None

# Testing both functions
if __name__ == "__main__":
    start = 'A'
    goal = 'F'

    print("Graph:")
    for node in graph:
        print(f"{node}: {graph[node]}")

    print(f"\nStarting BFS from {start} to {goal}")
    bfs_result = bfs(graph, start, goal)
    print("BFS path:", bfs_result)

    print(f"\nStarting DFS from {start} to {goal}")
    dfs_result = dfs(graph, start, goal)
    print("DFS path:", dfs_result)
