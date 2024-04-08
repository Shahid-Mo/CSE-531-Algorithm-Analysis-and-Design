def solve_knapsack_unbounded_bottomup(profits, weights, capacity):
    """
    Solves the unbounded knapsack problem using bottom-up dynamic programming.
    
    Parameters:
        profits (list): List of item profits.
        weights (list): List of item weights.
        capacity (int): Maximum capacity of the knapsack.
    
    Returns:
        int: Maximum achievable profit.
        list: Indices of selected items.
    """
    n = len(profits)

    if capacity <= 0 or n == 0 or len(weights) != n:
        return 0, []

    dp = [[0 for _ in range(capacity + 1)] for _ in range(n)]

    for i in range(n):
        for c in range(1, capacity + 1):
            profit1 = dp[i][c - weights[i]] + profits[i] if weights[i] <= c else 0
            profit2 = dp[i - 1][c] if i > 0 else 0
            dp[i][c] = max(profit1, profit2)

    return dp[n - 1][capacity], _print_selected_items(dp, weights, capacity)

def _print_selected_items(dp, weights, capacity):
    """
    Helper function to determine the items included in the knapsack.
    """
    selected_items = []
    i = len(weights) - 1
    while i >= 0:
        if i == 0 or dp[i][capacity] != dp[i-1][capacity]:
            selected_items.append(i)
            capacity -= weights[i]
        else:
            i -= 1

    return selected_items[::-1]

# Example usage
if __name__ == "__main__":
    profits = [10, 18]
    weights = [30, 40]
    capacity = 100
    max_profit, selected_indices = solve_knapsack_unbounded_bottomup(profits, weights, capacity)
    print(f"Maximum Profit: {max_profit}")
    print(f"Selected Indices: {selected_indices}")
