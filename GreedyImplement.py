# GreedyImplement.py

from memory_profiler import profile
import random
import time

@profile
def generate_random_subsets(universe_size, num_subsets):
    universe = set(range(1, universe_size + 1))
    subsets = []
    costs = []
    for _ in range(num_subsets):
        subset_size = random.randint(1, min(10, universe_size)) 
        subset = set(random.sample(list(universe), subset_size))
        cost = random.uniform(1, 10) 
        subsets.append(subset)
        costs.append(cost)
    return subsets, costs

@profile
def greedy_set_cover(universe, subsets, costs):
    covered = set()
    cover = []
    total_cost = 0
    while covered != universe:
        max_ratio = -1
        best_subset_index = None
        for i, subset in enumerate(subsets):
            if subset - covered:  
                ratio = len(subset - covered) / costs[i]
                if ratio > max_ratio:
                    max_ratio = ratio
                    best_subset_index = i
        if best_subset_index is None:
           
            return cover, total_cost  
        cover.append(subsets[best_subset_index])
        covered |= subsets[best_subset_index]
        total_cost += costs[best_subset_index]
    return cover, total_cost

def main():
     # Set random
    random.seed(42) 
    sizes = [20, 200, 2000]
    for size in sizes:
        universe = set(range(1, size + 1))
        subsets, costs = generate_random_subsets(size, size // 2)  # Generate random subsets
        start_time = time.time()
        cover, cost = greedy_set_cover(universe, subsets, costs)
        end_time = time.time()
        print(f"Universe size: {size}, Cover found: {cover}, Total cost: {cost}, Time taken: {end_time - start_time}")

if __name__ == "__main__":
    main()
