def optimal_bst(keys, freq):
    n = len(keys)
    
    dp = [[0] * n for _ in range(n)]

    
    for i in range(n):
        dp[i][i] = freq[i]

    
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            dp[i][j] = float('inf')
            
            for r in range(i, j + 1):
                cost = sum(freq[k] for k in range(i, j + 1)) + \
                       (dp[i][r - 1] if r > i else 0) + \
                       (dp[r + 1][j] if r < j else 0)
                dp[i][j] = min(dp[i][j], cost)

    
    return dp[0][n - 1]


keys = list(map(int, input("Enter the keys separated by spaces: ").split()))
freq = list(map(int, input("Enter the frequencies separated by spaces: ").split()))


optimal_cost = optimal_bst(keys, freq)


print("Optimal cost:", optimal_cost)
