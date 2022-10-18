print('testing')

for i in range(10):
    print(' ' * (10 - i) + '*' * i, end=' ')
    print('*' * i + ' ' * (10 - i))

print()

for i in range(10, 0, -1):
    print(' ' * (10 - i) + '*' * i, end=' ')
    print('*' * i + ' ' * (10 - i))
