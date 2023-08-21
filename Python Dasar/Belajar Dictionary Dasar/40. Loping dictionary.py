teman_dict = {
'gun':'gunandi',
'bem':'abiem',
'mng':'lukman'
}



### Oprator untuk mengambil item / interables

# menggunakan keys()
keys = teman_dict.keys()
print(keys,'\n')

print('Ini adalah key nya:')
for key in teman_dict.keys():
	print(key)
print('\n')

# menggunakan values()
values = teman_dict.values()
print(values,'\n')

print('Ini adalah value nya:')
for value in teman_dict.values():
	print(value)
print('')

# menggunakan items()
items = teman_dict.items()
print(items)
print('')

print('Ini adalah item nya:')
for item in teman_dict.items():
	print(item)
print('')

#### menggabungkan keys,values dan items
print('key dan value menggunakan items:')
for key,value in teman_dict.items():
	print(f'key:{key} value:{value}')
