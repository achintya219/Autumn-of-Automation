def max_profit(price, s, e):
    if e <= s:
        return 0

    profit = 0
    for i in range(s, e):
        for j in range(i + 1, end + 1):
            if price[j] > price[i]:
                curr_profit = price[j] - price[i] + max_profit(price, s, i - 1) + max_profit(price, j + 1,
                                                                                                         e)
                day_to_buy.append(i)
                profit = max(profit, curr_profit)
    return profit


if __name__ == '__main__':
    day_to_buy = []
    n = int(input())
    prices = [int(i) for i in input().split()]
    print(max_profit(prices, 0, n - 1))
    print(day_to_buy[-1])