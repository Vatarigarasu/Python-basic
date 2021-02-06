def my_func(arg1, arg2, arg3):
    args = [arg1, arg2, arg3]
    args.sort(reverse=True)
    print(sum(args[0:2]))


arg1 = 8
arg2 = 4
arg3 = 7

my_func(arg1, arg2, arg3)
