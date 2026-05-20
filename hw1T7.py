def knapsack_01(goods, capacity):
    n = len(goods)
    # 初始化dp表
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        w, v = goods[i - 1]
        for j in range(1, capacity + 1):
            if j < w:
                # 装不下，只能不选
                dp[i][j] = dp[i - 1][j]
            else:
                # 选与不选取最大
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - w] + v)
    return dp[n][capacity]


# 数据
items = [(5, 10), (4, 40), (6, 30), (3, 50)]
max_cap = 9
max_val = knapsack_01(items, max_cap)
print(f"背包最大承重{max_cap}，可装最大价值：{max_val}")