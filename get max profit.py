def get_max_profit(value_list: list):
    profit = -float('inf')
    for i, number in enumerate(value_list):
        for j in range(i + 1, len(value_list)):
            if value_list[j] - number > profit:
                profit = value_list[j] - number

    return profit


def get_max_profit_on(value_list):
    max_profit = float('-inf')
    current_profit = 0

    for value in value_list:
        current_profit = max(value, current_profit + value)
        max_profit = max(max_profit, current_profit)

    return max_profit


b = [1, 5, 6, 46, 7, 8, 9, 9, 101, 4, 56, 45, 447]


# print(get_max_profit(b))


def k_bonacci(n: int, k: int):
    ls = [i for i in range(k)]
    print(ls)
    for i in range(n - k):
        temp = 0
        for j in range(-1, -k - 1, -1):
            temp += ls[j]
        print(temp)
        ls.append(temp)
    print(ls)
    return ls[-1]


print(k_bonacci(100, 2))
