import random

# GENETIC ALGORITHM FUNCTIONS

def fitness(route, routes):
    return 1 / routes[route]["distance"]

def select_parents(pop):
    return random.sample(pop, 2)

def crossover(p1, p2):
    return random.choice([p1, p2])

def mutate(route, population, mutation_rate=0.3):
    return random.choice(population) if random.random() < mutation_rate else route

def genetic_algorithm(routes, generations=5):
    population = list(routes.keys())
    for _ in range(generations):
        population = [mutate(crossover(*select_parents(population)), population) 
                      for _ in population]
    return min(population, key=lambda r: routes[r]["distance"])


# EXAMPLE 1: Package Delivery
routes_example1 = {
    "Route A": {"path": "Depot → Factory → Client", "distance": 14},
    "Route B": {"path": "Depot → Store → Client", "distance": 9},
    "Route C": {"path": "Depot → Market → Client", "distance": 11},
    "Route D": {"path": "Depot → Warehouse → Client", "distance": 7}
}

best1 = genetic_algorithm(routes_example1)

print("\n=== Example 1: Package Delivery ===")
print(f"{'Route':<12} | {'Distance (km)':<13} | Path")
print("-" * 50)
for r, info in routes_example1.items():
    mark = "✅" if r == best1 else " "
    print(f"{r:<12} | {info['distance']:<13} | {info['path']} {mark}")
print(f"\nBest Route: {best1} → {routes_example1[best1]['path']} ({routes_example1[best1]['distance']} km)")

# EXAMPLE 2: Food Delivery
routes_example2 = {
    "Route 1": {"path": "Bakery → Cafe → Apartment", "distance": 6},
    "Route 2": {"path": "Bakery → Park → Apartment", "distance": 10},
    "Route 3": {"path": "Bakery → Library → Apartment", "distance": 8},
    "Route 4": {"path": "Bakery → School → Apartment", "distance": 12}
}

best2 = genetic_algorithm(routes_example2)

print("\n=== Example 2: Food Delivery ===")
print(f"{'Route':<12} | {'Distance (km)':<13} | Path")
print("-" * 50)
for r, info in routes_example2.items():
    mark = "✅" if r == best2 else " "
    print(f"{r:<12} | {info['distance']:<13} | {info['path']} {mark}")
print(f"\nBest Route: {best2} → {routes_example2[best2]['path']} ({routes_example2[best2]['distance']} km)")