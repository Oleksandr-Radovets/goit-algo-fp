import uuid
import networkx as nx
import matplotlib.pyplot as plt

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

# Функція для малювання дерева
def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}  # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()

# Створення бінарної купи
class BinaryHeap:
    def __init__(self):
        self.heap = []

    def _heapify_up(self, index):
        while index > 0:
            parent_index = (index - 1) // 2
            if self.heap[index].val < self.heap[parent_index].val:
                # Міняємо місцями
                self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
                index = parent_index
            else:
                break

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if left_child_index < len(self.heap) and self.heap[left_child_index].val < self.heap[smallest].val:
            smallest = left_child_index

        if right_child_index < len(self.heap) and self.heap[right_child_index].val < self.heap[smallest].val:
            smallest = right_child_index

        if smallest != index:
            # Міняємо місцями
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self._heapify_down(smallest)

    def insert(self, key):
        new_node = Node(key)
        self.heap.append(new_node)
        self._heapify_up(len(self.heap) - 1)

    def remove_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return root

    def build_heap(self, elements):
        for element in elements:
            self.insert(element)

    def get_root(self):
        return self.heap[0] if self.heap else None

# Приклад використання бінарної купи
heap = BinaryHeap()
heap.insert(10)
heap.insert(4)
heap.insert(15)
heap.insert(20)
heap.insert(8)
heap.insert(30)

# Малюємо візуалізацію бінарної купи
draw_tree(heap.get_root())
