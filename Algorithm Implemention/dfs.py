def dfs(graph, start):
    visited = set()
    result = []
    
    def dfs_recursive(node):
        visited.add(node)
        result.append(node)
        
        for neighbor in graph[node]:
            if neighbor not in visited:
                dfs_recursive(neighbor)
    
    dfs_recursive(start)
    return result

# Taking user input for graph (same as BFS)
graph = {}
nodes = int(input("Enter number of nodes: "))

for i in range(nodes):
    node = input(f"Enter node {i+1}: ")
    connections = input(f"Enter connections for node {node} (comma-separated): ").split(',')
    graph[node] = [conn.strip() for conn in connections if conn.strip()]

start_node = input("Enter start node: ")

# Performing DFS
dfs_result = dfs(graph, start_node)
print("DFS traversal:", ' -> '.join(dfs_result))