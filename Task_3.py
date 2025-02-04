import heapq

# Алгоритм Дейкстри
def dijkstra(graph, start):
    # Відстань до кожної вершини від початкової (по замовчуванню нескінченність)
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0

    # Бінарна купа для вибору вершини з мінімальною відстанню
    priority_queue = [(0, start)]  # (відстань, вершина)

    while priority_queue:
        # Вибираємо вершину з мінімальною відстанню
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Якщо поточна відстань більша за вже знайдену (потрібно пропустити)
        if current_distance > distances[current_vertex]:
            continue

        # Перевіряємо сусідів поточної вершини
        for neighbor, weight in graph[current_vertex].items():
            distance = current_distance + weight

            # Якщо знайдений більш короткий шлях до сусіда
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

# Приклад зваженого графа
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Виклик алгоритму Дейкстри з початковою вершиною 'A'
start_vertex = 'A'
distances = dijkstra(graph, start_vertex)

# Виведення результату
print(f"Найкоротші відстані від вершини {start_vertex}:")
for vertex, distance in distances.items():
    print(f"{vertex}: {distance}")
