for i in range(2):
    value = int(input('Enter an integer (-1 to break): '))
    print('You entered:', value)

    if value == -1:
        break
else:
    print('The loop terminated without executing the break')

#I observed that if i enter normal numbers, the loop ends and the else message prints but if i eneter -1 it breaks
