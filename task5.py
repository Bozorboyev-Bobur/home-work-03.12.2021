def calcSumBetween(x, y):
    acc = 0
    for i in range(x + 1, y):
        acc += i
    return acc

print(calcSumBetween(10, 15))