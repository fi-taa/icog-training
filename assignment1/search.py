from collections import deque

def bfs(graph, source, destination):
    """
    Perform Breadth-First Search (BFS) on the graph from source to destination.
    
    :param graph: Graph object.
    :param source: Starting city.
    :param destination: Destination city.
    :return: List of cities representing the shortest path from source to destination, or empty if no path.
    """
    visited = set()  # Set to keep track of visited nodes.
    queue = deque([(source, [source])])  # Initialize the queue with source and its path
    levels = [[]]  # List to store nodes explored at each level

    while queue:
        current, path = queue.popleft()
        if current == destination:
            # Destination found, return the path
            levels[len(path) - 1].append(current)
            return path, levels

        if current in visited:
            continue  # Skip already visited nodes

        visited.add(current)
        levels[len(path) - 1].append(current)

        for neighbor in graph.adjacency_list.get(current, []):
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))
                if len(levels) == len(path):
                    levels.append([])

    return [], []  # No path found

def dfs(graph, source, destination):
    """
    Perform Depth-First Search (DFS) on the graph from source to destination.
    
    :param graph: Graph object.
    :param source: Starting city.
    :param destination: Destination city.
    :return: List of cities representing the path from source to destination, or empty if no path.
    """
    stack = [source]
    visited = {source: None}

    while stack:
        current = stack.pop()

        if current == destination:
            # Construct the path from source to destination
            final_path = []
            while current is not None:
                final_path.append(current)
                current = visited[current]
            return final_path[::-1]

        for neighbor in graph.adjacency_list.get(current, []):
            if neighbor not in visited:
                visited[neighbor] = current
                stack.append(neighbor)

    return []  # No path found
