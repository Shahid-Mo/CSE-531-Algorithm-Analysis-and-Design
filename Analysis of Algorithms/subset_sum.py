def subset_sum_maximize_weight(weights, W):
    """
    Solves the Subset Sum problem to maximize the total weight of the selected items without exceeding the given capacity.
    
    Parameters:
    weights (list): List of weights of items.
    W (int): Capacity of the subset sum.
    
    Returns:
    int: Maximum total weight of the selected items.
    list: Indices of the selected items.
    """
    n = len(weights)
    dp = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(dp[i - 1][w], weights[i - 1] + dp[i - 1][w - weights[i - 1]])
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Extract the selected items
    selected_items = []
    w = W
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
    
    return dp[n][W], selected_items[::-1]

# Example usage
if __name__ == '__main__':
    weights = [2, 1, 3, 4]
    W = 5
    optimal_weight, selected_items = subset_sum_maximize_weight(weights, W)
    print("Optimal Weight:", optimal_weight)
    print("Selected Items:", selected_items)
