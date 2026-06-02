def knapsackDP(items: list[list[int]], capacity: int)->int:
    n = len(items)
    dp = [[0 for _ in range(capacity+1)] for _ in range(n+1)]
    for i, item in enumerate(items):
        for j in range(item[0], capacity+1):
            dp[i+1][j] = max(
                dp[i][j],
                dp[i][j-item[0]] + item[1]
            )
    max_value = 0
    for i in range(capacity+1):
        max_value = max(max_value, dp[n][i])
    return max_value

def knapsackDP_improvement_space(items: list[list[int]], capacity: int)->int:
    n = len(items)
    dp = [0 for _ in range(capacity+1)]
    for item in items:
        for j in range(capacity, item[0]-1, -1):
            dp[j] = max(
                dp[j],
                dp[j-item[0]] + item[1]
            )
    max_value = 0
    for i in range(capacity+1):
        max_value = max(max_value, dp[i])
    return max_value

data = [
    [10, 60],
    [20, 100],
    [30, 120],
    [15, 70],
    [25, 80],
    [35, 150]
]

capacity = 50

print(knapsackDP(data, capacity))
print(knapsackDP_improvement_space(data, capacity))