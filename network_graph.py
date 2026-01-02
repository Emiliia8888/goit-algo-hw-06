import matplotlib.pyplot as plt
import networkx as nx

def create_security_network():
    G = nx.Graph()

    nodes = {
        "Internet Gateway": "gateway",
        "Web Server": "server",
        "VPN Server": "server",
        "Auth Server": "server",
        "Sensitive Database": "database",
        "HR Workstation": "workstation",
        "HR File Server": "server",
        "Engineering Workstation": "workstation",
        "Dev Build Server": "server",
    }

    for node, device_type in nodes.items():
        G.add_node(node, device_type=device_type)

    # Weighted edges (represent risk)
    edges = [
        ("Internet Gateway", "Web Server", 1),
        ("Internet Gateway", "VPN Server", 2),
        ("Web Server", "Auth Server", 3),
        ("Auth Server", "Sensitive Database", 1),
        ("Web Server", "HR Workstation", 2),
        ("HR Workstation", "HR File Server", 2),
        ("Web Server", "Engineering Workstation", 1),
        ("Engineering Workstation", "Dev Build Server", 1),
        ("Dev Build Server", "Sensitive Database", 5),  # risky shortcut
    ]

    for u, v, w in edges:
        G.add_edge(u, v, weight=w)

    return G


def visualize(G):
    pos = {
        "Internet Gateway": (0, 2),
        "Web Server": (1, 2),
        "VPN Server": (0, 1),
        "Auth Server": (2, 2),
        "Sensitive Database": (3, 2),
        "HR Workstation": (2, 1),
        "HR File Server": (3, 1),
        "Engineering Workstation": (1, 1),
        "Dev Build Server": (2, 0),
    }

    color_map = {
        "gateway": "orange",
        "server": "lightblue",
        "workstation": "lightgreen",
        "database": "red",
    }

    node_colors = [
        color_map[G.nodes[n]["device_type"]] for n in G.nodes()
    ]

    plt.figure(figsize=(10, 6))
    nx.draw(
        G,
        pos,
        with_labels=True,
        node_color=node_colors,
        node_size=2200,
        edge_color="gray"
    )

    plt.title("Multi-Department Security Network")
    plt.show()

if __name__ == "__main__":
    visualize(create_security_network())
