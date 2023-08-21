print('object identify is'.center(60,':'))

x = 10
y = 10

print(f'id {x} = {hex(id(x))}')
print(f'id {x} = {hex(id(y))}')
print('')
print(f'Apakah {x} is {y}? {x is y}')

x = 20
print(f'Apakah {x} is {y}? {x is y}')
print('')


print('object identify is not'.center(60,':'))

x = 10
y = 20

print(f'id {x} = {hex(id(x))}')
print(f'id {x} = {hex(id(y))}')
print('')

print(f'Apakah {x} is not {y}? {x is not y}')

x  = 20
print(f'Apakah {x} is not {y}? {x is not y}')


