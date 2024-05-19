import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Graph:
    """Graph data structure, undirected by default."""
    
    def __init__(self):
        """Initialize an empty graph."""
        self.adjacency_list = {}

    def add_edge(self, source, destination):
        """Add an edge between source and destination."""
        if source not in self.adjacency_list:
            self.adjacency_list[source] = []
        if destination not in self.adjacency_list:
            self.adjacency_list[destination] = []
        self.adjacency_list[source].append(destination)
        self.adjacency_list[destination].append(source)  # For undirected graph

    def __str__(self):
        """Return a string representation of the graph."""
        return '\n'.join([f'{city}: {neighbors}' for city, neighbors in self.adjacency_list.items()])

    def __repr__(self):
        """Return a detailed string representation of the graph."""
        return f'Graph(adjacency_list={self.adjacency_list})'

    def draw(self, path=None, title="City Connections Graph"):
        """Draw the graph using networkx and matplotlib."""
        G = nx.Graph()
        for city, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                G.add_edge(city, neighbor)
        
        pos = nx.spring_layout(G)  # positions for all nodes
        plt.figure(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold")
        
        if path:
            path_edges = list(zip(path, path[1:]))
            nx.draw_networkx_nodes(G, pos, nodelist=path, node_color="red")
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
        
        plt.title(title)
        plt.show()

    def animate_bfs(self, path, levels, title="Animation of BFS"):
        """Animate the BFS search path using networkx and matplotlib."""
        G = nx.Graph()
        for city, neighbors in self.adjacency_list.items():
            for neighbor in neighbors:
                G.add_edge(city, neighbor)
        
        pos = nx.spring_layout(G)  # positions for all nodes

        fig, ax = plt.subplots(figsize=(10, 7))
        nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", ax=ax)
        
        def update(num):
            ax.clear()
            nx.draw(G, pos, with_labels=True, node_size=3000, node_color="lightblue", font_size=10, font_weight="bold", ax=ax)
            
            for level in range(num + 1):  # Iterate over each level up to num
                nodes_at_level = levels[level]
                nx.draw_networkx_nodes(G, pos, nodelist=nodes_at_level, node_color="red", ax=ax)
            
            # Draw the path edges
            path_edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
            nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
            
            plt.title(title)

        ani = FuncAnimation(fig, update, frames=len(levels), interval=1000, repeat=False)
        plt.show()
