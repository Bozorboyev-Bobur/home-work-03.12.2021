signs = {
    'add': '+',
    'subtract': '-',
}

def calculator(a, b, action):
    return eval(f'{a}{signs.get(action)}{b}')


print(calculator(2,3, 'add'))
print(calculator(2,3, 'subtract'))

