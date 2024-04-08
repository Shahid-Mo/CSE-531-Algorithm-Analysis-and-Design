def lcs(x, y):
    """
    Finds and returns the longest common subsequence between two strings.

    Parameters:
        x (str): The first string.
        y (str): The second string.

    Returns:
        str: The longest common subsequence (LCS) of x and y.
    """
    n, m = len(x), len(y)  # Length of the input strings
    # Initialize a matrix to store the lengths of longest common subsequences
    t = [[0 for _ in range(m+1)] for _ in range(n+1)]

    # Fill the matrix using bottom-up DP approach
    for i in range(1, n+1):
        for j in range(1, m+1):
            if x[i-1] == y[j-1]:
                t[i][j] = 1 + t[i-1][j-1]
            else:
                t[i][j] = max(t[i][j-1], t[i-1][j])

    # Reconstruct the LCS from the matrix
    lcs_string = ''
    i, j = n, m
    while i > 0 and j > 0:
        if x[i-1] == y[j-1]:  # If characters match, it's part of LCS
            lcs_string += x[i-1]
            i -= 1
            j -= 1
        elif t[i-1][j] > t[i][j-1]:  # Move in the direction of greater value
            i -= 1
        else:
            j -= 1

    return lcs_string[::-1]  # Return the reversed LCS string

# Example usage
if __name__ == "__main__":
    x = 'acbcf'
    y = 'abcdaf'
    print("LCS:", lcs(x, y))
