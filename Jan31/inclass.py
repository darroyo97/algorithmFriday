for a in range(1, 1001):
    for b in range(a + 1, a + 1001):
        if a + b > 1000:
            break
        c = 1000 - a - b
        if (a ** 2 + b ** 2 == c ** 2):
            print(f'The number is {a}+{b}+{c} = 1000')
