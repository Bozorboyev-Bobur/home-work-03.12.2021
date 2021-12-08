def end_zeros(num: int):
    zeros = 0
    num = str(num)
    if num [-1] != '0': return 0

    for i in range(len(num) -1, -1, -1):
        if num[i] == '0':
            zeros += 1
        else: return zeros
    return zeros

print(end_zeros(0))
print(end_zeros(1))
print(end_zeros(10))
print(end_zeros(101))
