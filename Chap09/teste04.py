a = [10, 20, ['a', 'b']]
b = a[:]
print(f'a - {a}')
print(f'b - {b}')

a[1] = 5
a[2][0] = 'x'

print(f'a - {a}')
print(f'b - {b}')
