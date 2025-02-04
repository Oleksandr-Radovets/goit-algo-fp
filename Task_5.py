import uuid
import networkx as nx
import matplotlib.pyplot as plt
import random


# Клас для вузла дерева
class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color  # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4())  # Унікальний ідентифікатор для кожного вузла


# Додавання ребер до графа для візуалізації
def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)  # Використання id та збереження значення вузла
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


# Генерація унікальних кольорів для відображення порядку відвідування
def generate_color(depth, max_depth):
    r = int((depth / max_depth) * 255)
    g = int((1 - depth / max_depth) * 255)
    b = 128  # Постійна складова для синіх відтінків
    return f"#{r:02X}{g:02X}{b:02X}"


# Функція для візуалізації дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


# Обхід в глибину (DFS) за допомогою стеку
def dfs(tree_root):
    stack = [tree_root]
    visited = []
    max_depth = 0
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            depth = len(visited) - 1
            node.color = generate_color(depth, len(visited))
            max_depth = max(max_depth, depth)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

    return visited


# Обхід в ширину (BFS) за допомогою черги
def bfs(tree_root):
    queue = [tree_root]
    visited = []
    max_depth = 0
    while queue:
        node = queue.pop(0)
        if node not in visited:
            visited.append(node)
            depth = len(visited) - 1
            node.color = generate_color(depth, len(visited))
            max_depth = max(max_depth, depth)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return visited


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Візуалізація дерева після DFS обходу
dfs(root)
draw_tree(root)

# Візуалізація дерева після BFS обходу
bfs(root)
draw_tree(root)
