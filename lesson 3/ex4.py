def my_func(a1, a2):
    res = a1
    for i in range(a2-1):
        res *= a1
    print(res)


a1 = float(644.45)
a2 = int(14)
my_func(a1, a2)
