### copy dan pop  dictionary


teman_teman = {
'gun':'gunandi',
'bem':'abiem',
'mng':'lukman',
'lid':'holid',
'na':'diana'
}

# copy dictionary jika kita change friends tman" tdk ikt brbh
friends = teman_teman.copy()

print('Teman teman: \n',teman_teman)
print('\n')
print('Friends:\n',friends)
print('\n')
# pop() mengambil data .pop('key')
pop = friends.pop('na')
print('dictionary yg di pop:',pop)
print('')
print('Setelah di pop:\n',friends)
print('')
# popitem() mengambil dictionary paling belakang/akhir
popitem = friends.popitem()
print('dictionary popitem():\n',popitem)
print('')
print('Setalah di pop:\n',friends)