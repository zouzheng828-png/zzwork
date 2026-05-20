def max_profit_dates(profits):
    n = len(profits)
    prefix = 0                # 当前前缀和
    min_prefix = 0            # 当前最小前缀和
    min_prefix_index = 0      # 最小前缀和对应的索引（前缀和数组的索引）
    max_profit = -float('inf')
    buy_day = sell_day = -1   # 最终买入/卖出日（前缀和数组索引形式）

    for i in range(1, n + 1):     # i 是当前考虑的前缀和数组索引（1..n）
        prefix += profits[i - 1]  # profits[i-1] 是原数组的第 i-1 天

        # 当前可得到利润
        profit = prefix - min_prefix
        if profit > max_profit:
            max_profit = profit
            sell_day = i            # 卖出日在原数组第 i 天（因为 prefix[i] 表示前 i 天利润）
            buy_day = min_prefix_index + 1  # 买入日是原数组第 min_prefix_index 天的下一天吗？小心

        # 更新最小前缀和
        if prefix < min_prefix:
            min_prefix = prefix
            min_prefix_index = i

    # buy_day 对应原数组中买入天（1-based）
    # sell_day 对应原数组中卖出天（1-based）
    # 检查例子 profits=[3,2,1,-7,5,2,-1,3,-1]
    # buy_day = 5, sell_day = 8 对应 profits[4..7] 的和为 5+2+(-1)+3 = 9
    return max_profit, buy_day, sell_day


if __name__ == "__main__":
    profits = [3, 2, 1, -7, 5, 2, -1, 3, -1]
    profit, buy, sell = max_profit_dates(profits)
    print(f"最大收益: {profit}")
    print(f"买入日: {buy}, 卖出日: {sell}")
    # 验证 sum(profits[buy-1:sell]) 看是否等于 profit
    print("验证收益:", sum(profits[buy-1:sell]))