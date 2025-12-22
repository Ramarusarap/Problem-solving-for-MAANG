dp = [0] * (n + 2)

for i in range(n - 1, -1, -1):
    take = value[i] + dp[i + 2]
    skip = dp[i + 1]
    dp[i] = max(take, skip)

return dp[0]
