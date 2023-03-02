def count_ways(n, coins):
    table = [0] * (n + 1)
    table[0] = 1
    for coin in coins:
        for i in range(coin, n + 1):
            table[i] += table[i - coin]
    return table[n]

coins = [1, 2, 5, 10, 20, 50, 100, 200]
n = 200
print(count_ways(n, coins))