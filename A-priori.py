from itertools import combinations
from collections import defaultdict


def apriori_analysis(data, min_support, min_confidence):
    total = len(data)
    
    # Count single items
    item_count = defaultdict(int)
    for transaction in data:
        for item in transaction:
            item_count[frozenset([item])] += 1

    # Filter itemsets by support threshold
    def filter_support(candidates):
        return {item: count for item, count in candidates.items() if count / total >= min_support}

    # Generate candidate itemsets of size k
    def generate_candidates(prev_frequent, k):
        keys = list(prev_frequent.keys())
        candidates = defaultdict(int)
        for i in range(len(keys)):
            for j in range(i + 1, len(keys)):
                union = keys[i] | keys[j]
                if len(union) == k:
                    for transaction in data:
                        if union.issubset(transaction):
                            candidates[union] += 1
        return candidates

    # Generate association rules from frequent itemsets
    def generate_rules(frequent_sets, all_support):
        rules = []
        for itemset in frequent_sets:
            if len(itemset) < 2:
                continue
            for size in range(1, len(itemset)):
                for antecedent in combinations(itemset, size):
                    antecedent = frozenset(antecedent)
                    consequent = itemset - antecedent
                    if antecedent in all_support and all_support[antecedent] > 0:
                        confidence = all_support[itemset] / all_support[antecedent]
                        support = all_support[itemset] / total
                        if confidence >= min_confidence:
                            rules.append((antecedent, consequent, support, confidence))
        return rules

    # Main Apriori loop
    all_support = {}
    k = 1
    current_frequent = filter_support(item_count)
    all_support.update(current_frequent)
    all_frequent = dict(current_frequent)

    while current_frequent:
        k += 1
        candidates = generate_candidates(current_frequent, k)
        current_frequent = filter_support(candidates)
        all_support.update(current_frequent)
        all_frequent.update(current_frequent)

    rules = generate_rules(all_frequent, all_support)
    return all_frequent, rules, total


# -------
# EXAMPLE 1: Restaurant Menu Recommendations
# -----------------------------
print("="*60)
print("EXAMPLE 1: Restaurant Menu Recommendations")

restaurant_data = [
    {'burger', 'fries', 'soda'},
    {'pizza', 'soda'},
    {'burger', 'fries'},
    {'burger', 'fries', 'salad'},
    {'pizza', 'fries', 'soda'},
    {'salad', 'water'},
    {'burger', 'soda'},
    {'burger', 'fries', 'soda'},
]

freq1, rules1, n1 = apriori_analysis(restaurant_data, min_support=0.3, min_confidence=0.6)

# --- Display frequent itemsets ---
print(f"\nTotal Orders: {n1} | Min Support: 30% | Min Confidence: 60%\n")
print("{:<25} {:<10}".format("Frequent Itemset", "Support"))
print("-"*40)
for items, count in sorted(freq1.items(), key=lambda x: -x[1]):
    print("{:<25} {:<10.2f}".format(str(set(items)), count/n1))

# --- Display association rules ---
print("\n{:<25} {:<25} {:<10} {:<10}".format("Antecedent", "Consequent", "Support", "Confidence"))
print("-"*70)
for ant, con, sup, conf in sorted(rules1, key=lambda x: -x[3]):
    print("{:<25} {:<25} {:<10.2f} {:<10.2f}".format(str(set(ant)), str(set(con)), sup, conf))


# -----------------------------
# EXAMPLE 2: Student Course Enrollment Patterns
# -----------------------------
print("\n" + "="*60)
print("EXAMPLE 2: Student Course Enrollment Patterns")

course_data = [
    {'Math', 'Physics'},
    {'Math', 'Computer Science'},
    {'Physics', 'Chemistry'},
    {'Math', 'Physics', 'Computer Science'},
    {'Math', 'Chemistry'},
    {'Computer Science', 'Chemistry'},
    {'Math', 'Physics'},
    {'Physics', 'Computer Science'},
]

freq2, rules2, n2 = apriori_analysis(course_data, min_support=0.3, min_confidence=0.6)

# --- Display frequent course combinations ---
print(f"\nTotal Students: {n2} | Min Support: 30% | Min Confidence: 60%\n")
print("{:<30} {:<10}".format("Frequent Course Combinations", "Support"))
print("-"*45)
for items, count in sorted(freq2.items(), key=lambda x: -x[1]):
    print("{:<30} {:<10.2f}".format(str(set(items)), count/n2))

# --- Display course recommendation rules ---
print("\n{:<25} {:<25} {:<10} {:<10}".format("Antecedent", "Consequent", "Support", "Confidence"))
print("-"*70)
for ant, con, sup, conf in sorted(rules2, key=lambda x: -x[3]):
    print("{:<25} {:<25} {:<10.2f} {:<10.2f}".format(str(set(ant)), str(set(con)), sup, conf))