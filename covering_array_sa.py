import numpy as np
import random
import math

def initialize_matrix(rows, cols):
    """Generate a random binary matrix with given dimensions."""
    return np.random.randint(2, size=(rows, cols))

def determine_N(k):
    """Calculate the required number of rows based on k."""
    return int(2.5 * k)
def evaluate_coverage(matrix):
    """
    Compute the number of uncovered parameter pairs in the given matrix.
    The function iterates over the matrix and checks for missing value pairs.
    """
    N, k = matrix.shape
    uncovered_count = 0

    # Iterating through rows to check for unique combinations
    for i in range(N - 1):
        subset = matrix[i:i + 2, :]
        unique_combos = set(tuple(subset[j, :]) for j in range(2))
        uncovered_count += 4 - len(unique_combos)  # Expecting 4 unique binary pairs

    return uncovered_count

def modify_neighbor(matrix, col_idx):
    """
    Generate a neighboring solution by modifying a randomly chosen column.
    This introduces slight variation while maintaining structure.
    """
    modified_matrix = matrix.copy()
    rows, _ = matrix.shape
    for i in range(rows):
        modified_matrix[i, col_idx] = 1 - modified_matrix[i, col_idx]  # Flip bit
    return modified_matrix

def simulated_annealing(k, max_iterations, freeze_limit):
    """
    Perform the Simulated Annealing algorithm to generate a covering array.
    """
    N = determine_N(k)
    T = k
    cooling_factor = 0.99
    freeze_counter = 0

    # Initialize a random starting matrix
    best_solution = initialize_matrix(N, k)
    best_score = evaluate_coverage(best_solution)

    for iteration in range(max_iterations):
        current_solution = best_solution.copy()
        column_idx = random.randint(0, k - 1)
        neighbor_solution = modify_neighbor(current_solution, column_idx)

        current_score = evaluate_coverage(current_solution)
        neighbor_score = evaluate_coverage(neighbor_solution)

        # Acceptance criteria based on SA probability
        if neighbor_score < current_score or \
                random.uniform(0, 1) < math.exp((current_score - neighbor_score) / T):
            current_solution = neighbor_solution.copy()

            if neighbor_score < best_score:
                best_solution = neighbor_solution.copy()
                best_score = neighbor_score
                freeze_counter = 0  # Reset freeze count on improvement
        else:
            freeze_counter += 1

        # Termination condition if the solution doesn't improve
        if freeze_counter >= freeze_limit:
            break

        # Cooling step
        T *= cooling_factor

    return best_solution, iteration + 1, "solution" if freeze_counter < freeze_limit else "frozen"

# Experiment Execution
test_k_values = [5, 6, 7]
max_iterations = 1000
freeze_threshold = 10

for k in test_k_values:
    total_iterations = 0
    for _ in range(30):
        result, iterations, termination_reason = simulated_annealing(k, max_iterations, freeze_threshold)
        total_iterations += iterations
        print(f"For k={k}, Iterations: {iterations}, Termination: {termination_reason}")
        print("Generated Covering Array:")
        print(result)
        
        # If the solution froze, show the final frozen state
        if termination_reason == "frozen":
            frozen_result, _, _ = simulated_annealing(k, max_iterations, freeze_threshold)
            print("Frozen State Covering Array:")
            print(frozen_result)

        print("=" * 50)
    
    avg_iterations = total_iterations / 30
    print(f"Average Iterations for k={k}: {avg_iterations}")
