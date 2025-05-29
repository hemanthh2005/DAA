def knapsack(w, wt, val, n):
    k = [[0 for _ in range(w + 1)] for _ in range(n + 1)]
    for i in range(n + 1):
        for j in range(w + 1):
            if i == 0 or j == 0:
                k[i][j] = 0
            elif wt[i - 1] <= j:
                k[i][j] = max(val[i - 1] + k[i - 1][j - wt[i - 1]], k[i - 1][j])
            else:
                k[i][j] = k[i - 1][j]
    return k[n][w]

# Driver code
val = [12,10,20,15]
wt = [2,1,3,2]
w = 5
n = len(val)

print("Optimal Profit using Knapsack (DP):", knapsack(w, wt, val, n))