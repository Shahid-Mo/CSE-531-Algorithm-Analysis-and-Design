def knapSack(W, wt, val, n):
    """
    Solves the 0-1 Knapsack problem.

    Parameters:
    W (int): Maximum weight of the knapsack.
    wt (list): List of weights of items.
    val (list): List of values of items.
    n (int): Number of items.
    
    Returns:
    int: Maximum value that can be accommodated in the knapsack.
    """
    K = [[0 for _ in range(W + 1)] for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for w in range(1, W + 1):
            if wt[i - 1] <= w:
                K[i][w] = max(K[i - 1][w], val[i - 1] + K[i - 1][w - wt[i - 1]])
            else:
                K[i][w] = K[i - 1][w]
    
    return K[n][W]

# Example usage
if __name__ == '__main__':
    profit = [60, 100, 120]
    weight = [10, 20, 30]
    W = 50
    n = len(profit)
    print(knapSack(W, weight, profit, n))
