def knapSack(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i-1] <= w:
                K[i][w] = max(val[i-1] + K[i-1][w-wt[i-1]], K[i-1][w])
            else:
                K[i][w] = K[i-1][w]

    return K[n][W]

# Taking inputs from the user
n = int(input("Enter the number of items: "))
val = list(map(int, input("Enter the values of the items separated by space: ").split()))
wt = list(map(int, input("Enter the weights of the items separated by space: ").split()))
W = int(input("Enter the capacity of the knapsack: "))

print(knapSack(W, wt, val, n))

