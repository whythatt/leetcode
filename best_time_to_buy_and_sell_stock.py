prices = [4, 2, 5, 3, 1, 3, 1]
profit = 0
buy = prices[0]
for i in prices[1:]:
    if i > buy:
        profit = max(profit, i - buy)
    else:
        buy = i
print(profit)
print(max(1, 2, 3, 4, 5))
