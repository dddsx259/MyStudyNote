def job_scheduling(items: list[tuple[tuple[int, int], int]]):
    items.sort(key = lambda x: x[0][1])
    n = len(items)
    p = []
    dp = [0]
    for i in range(n):
        start_time = items[i][0][0]
        closest_finish_item = -1
        for j in range(i-1, -1, -1):
            if items[j][0][1] <= start_time:
                closest_finish_item = j
                break
        p.append(closest_finish_item)
    for i in range(1, n+1):
        dp.append(
            max(
                dp[i-1],
                dp[p[i-1] + 1] + items[i-1][1]
            )
        )
    return dp[n]

items = [
    ((1, 4), 50),   # A
    ((3, 5), 20),   # B
    ((4, 6), 30),   # C
    ((5, 7), 40)    # D
]

print(job_scheduling(items))