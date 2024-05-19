from graph import Graph
from search import bfs, dfs

def read_cities(file_path):
    """
    Read cities and their connections from a file and return a Graph object.
    
    :param file_path: Path to the file containing city connections.
    :return: A Graph object representing the cities and their connections.
    """
    graph = Graph()
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:  # Skip the header line
            source, destination = line.strip().split(',')
            graph.add_edge(source, destination)
    return graph

if __name__ == "__main__":
    graph = read_cities('cities.txt')
    print("Graph representation:")
    print(graph)

    # Draw the original graph
    graph.draw()

    source_city = 'New York'
    destination_city = 'Seattle'  # Corrected the spelling here

    print(f"\nBFS from {source_city} to {destination_city}:")
    bfs_path, bfs_levels = bfs(graph, source_city, destination_city)
    print(bfs_path)
    if bfs_path:
        graph.animate_bfs(bfs_path, bfs_levels, title="BFS Path from New York to Seattle")

    print(f"\nDFS from {source_city} to {destination_city}:")
    dfs_path = dfs(graph, source_city, destination_city)
    print(dfs_path)
    if dfs_path:
        graph.animate_bfs(dfs_path, [dfs_path], title="DFS Path from New York to Seattle")
