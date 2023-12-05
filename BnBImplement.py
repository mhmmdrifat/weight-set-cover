import random
import time
from memory_profiler import profile

def generate_random_subsets(universe_size, num_subsets):
    universe = list(range(1, universe_size + 1))
    subsets = []
    costs = []
    for _ in range(num_subsets):
        subset_size = random.randint(1, universe_size // 2)
        subset = set(random.sample(universe, subset_size))
        cost = random.uniform(1, 10)
        subsets.append(subset)
        costs.append(cost)
    return subsets, costs

def bypassbranch(subset, i):
    for j in range(i - 1, -1, -1):
        if subset[j] == 0:
            subset[j] = 1
            return subset, j + 1
    return subset, 0

def nextvertex(subset, i, m):
    if i < m:
        subset[i] = 1 - subset[i]
        return subset, i + 1
    else:
        for j in range(m - 1, -1, -1):
            if subset[j] == 0:
                subset[j] = 1
                return subset, j + 1
    return subset, 0

@profile
def BB(universe, sets, costs):
    num_sets = len(sets)
    best_cost = sum(costs) 
    best_subset = [0] * num_sets
    
    stack = [([], 0)]
    
    while stack:
        current_subset, index = stack.pop()
        if index == num_sets:
            current_cost = sum(costs[i] for i, included in enumerate(current_subset) if included)
            if current_cost < best_cost:
                best_cost = current_cost
                best_subset = current_subset[:]
            continue
        stack.append((current_subset + [1], index + 1))
        stack.append((current_subset + [0], index + 1))
    
    return best_cost, best_subset

def main():
    random.seed(42)  
    sizes = [20, 200,2000]  
    
    for size in sizes:
        universe = set(range(1, size + 1))
        subsets, costs = generate_random_subsets(size, size // 2)
        subsets = [list(subset) for subset in subsets] 

        start_time = time.time()
        best_cost, best_subset = BB(universe, subsets, costs)
        end_time = time.time()

        if best_subset is not None:
            actual_subsets = [subsets[i] for i in range(len(best_subset)) if best_subset[i] == 1]
        else:
            actual_subsets = []
        
        print(f"Universe size: {size}")
        print(f"Best cost: {best_cost}")
        print(f"Best subset: {actual_subsets}")
        print(f"Time taken: {end_time - start_time:.4f} seconds\n")

if __name__ == "__main__":
    main()
