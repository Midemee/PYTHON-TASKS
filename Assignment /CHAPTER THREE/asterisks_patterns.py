for count in range(1,11):
    for number in range(count):
        print('*', end='')
    for number in range(10 - count):
        print(' ', end='')
    print(' ', end='')

    for number in range(10 - count + 1 ):
        print('*', end='')
    for number in range(count, -1):
        print(' ', end='')
    print(' ', end='')

    for number in range(count -1):
        print(' ', end='')
    for number in range(10 - count + 1 ):
        print('*', end='')
    for number in range(count -1):
        print(' ', end='')
    print(' ', end='')

    for number in range(10 - count):
        print(' ', end='')
    for number in range(count):
        print('*', end='')
    print()



