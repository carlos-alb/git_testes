for num in range(1,11):
    for x in range(1,11):
        print('%2d x %2d = %2d' %(num, x, (num*x)))
        if x == 10:
            print('=' *13)