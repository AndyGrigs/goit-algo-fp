import uuid
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import matplotlib.cm as cm

class Node:
    def __init__(self, key, color="#000000"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Колір вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes_colors):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [visited_nodes_colors.get(node[0], node[1]['color']) for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

def heap_to_tree(heap):
    if not heap:
        return None
    nodes = [Node(val) for val in heap]
    for i in range(len(heap)):
        left_index = 2 * i + 1
        right_index = 2 * i + 2
        if left_index < len(heap):
            nodes[i].left = nodes[left_index]
        if right_index < len(heap):
            nodes[i].right = nodes[right_index]
    return nodes[0]

def generate_color_gradient(n):
    norm = mcolors.Normalize(vmin=0, vmax=n)
    colormap = cm.get_cmap('Blues')
    return [mcolors.to_hex(colormap(norm(i))) for i in range(n)]

def traverse_in_order(node, visited, colors):
    if node is not None:
        traverse_in_order(node.left, visited, colors)
        visited.append(node)
        colors[node.id] = generate_color_gradient(len(visited))[len(visited) - 1]
        draw_tree(tree_root, colors)
        traverse_in_order(node.right, visited, colors)

def traverse_breadth_first(root, colors):
    if root is None:
        return
    queue = [root]
    visited = []
    while queue:
        node = queue.pop(0)
        visited.append(node)
        colors[node.id] = generate_color_gradient(len(visited))[len(visited) - 1]
        draw_tree(tree_root, colors)
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

# Приклад використання
heap = [10, 5, 20, 3, 8, 15, 30]
tree_root = heap_to_tree(heap)

# Візуалізація обходу в глибину
print("Обхід в глибину (In-Order):")
visited_colors_in_order = {}
traverse_in_order(tree_root, [], visited_colors_in_order)

# Візуалізація обходу в ширину
print("Обхід в ширину (Breadth-First):")
visited_colors_breadth_first = {}
traverse_breadth_first(tree_root, visited_colors_breadth_first)
