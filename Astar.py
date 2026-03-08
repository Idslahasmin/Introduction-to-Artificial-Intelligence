import heapq

# A* Search Algorithm
def a_star(graph, start, goal, heuristic):

    open_list = []
    heapq.heappush(open_list, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while open_list:

        _, current = heapq.heappop(open_list)

        # Goal reached → reconstruct path
        if current == goal:
            path = []
            while current:
                path.append(current)
                current = parent[current]
            return path[::-1]

        for neighbor, cost in graph[current]:

            new_cost = g_cost[current] + cost

            if neighbor not in g_cost or new_cost < g_cost[neighbor]:
                g_cost[neighbor] = new_cost
                f_cost = new_cost + heuristic[neighbor]
                heapq.heappush(open_list, (f_cost, neighbor))
                parent[neighbor] = current

    return None


# EXAMPLE 1: Navigation of Campus
print("A* EXAMPLE 1: Campus Navigation")

campus_graph = {
    'Gate': [('Cafeteria', 3), ('Gym', 6)],
    'Cafeteria': [('Library', 4)],
    'Gym': [('Library', 2)],
    'Library': []
}

campus_heuristic = {
    'Gate': 7,
    'Cafeteria': 4,
    'Gym': 2,
    'Library': 0
}

campus_path = a_star(campus_graph, 'Gate', 'Library', campus_heuristic)

print("Start Node :", 'Gate')
print("Goal Node  :", 'Library')
print("Shortest Path :", campus_path)


# EXAMPLE 2: Delivery Route
print("\n" + "=" * 55)
print("A* EXAMPLE 2: Delivery Route Optimization")

delivery_graph = {
    'Warehouse': [('Street1', 2), ('Street2', 5)],
    'Street1': [('Customer', 4)],
    'Street2': [('Customer', 1)],
    'Customer': []
}

delivery_heuristic = {
    'Warehouse': 6,
    'Street1': 3,
    'Street2': 2,
    'Customer': 0
}

delivery_path = a_star(delivery_graph, 'Warehouse', 'Customer', delivery_heuristic)

print("Start Node :", 'Warehouse')
print("Goal Node  :", 'Customer')
print("Shortest Path :", delivery_path)