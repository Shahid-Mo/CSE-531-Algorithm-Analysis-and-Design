def is_interleave(s1, s2, s3):
    """
    Determines if `s3` is an interleaving of `s1` and `s2`.
    
    Parameters:
        s1 (str): First input string.
        s2 (str): Second input string.
        s3 (str): Potential interleaving string.
    
    Returns:
        bool: True if `s3` is an interleaving of `s1` and `s2`, False otherwise.
    """
    if len(s1) + len(s2) != len(s3):
        return False

    dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]
    dp[0][0] = True

    for i in range(len(s1) + 1):
        for j in range(len(s2) + 1):
            if i > 0 and s1[i-1] == s3[i+j-1] and dp[i-1][j]:
                dp[i][j] = True
            if j > 0 and s2[j-1] == s3[i+j-1] and dp[i][j-1]:
                dp[i][j] = True

    return dp[-1][-1]

# Example usage
if __name__ == "__main__":
    s1 = 'aabcc'
    s2 = 'dbbca'
    s3 = 'aadbbcbcac'
    print(is_interleave(s1, s2, s3))
