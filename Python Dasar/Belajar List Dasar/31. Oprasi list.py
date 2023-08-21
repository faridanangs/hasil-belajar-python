#### Oprasi pada list

data_angka = [4,5,7,7,8,9,9,6,5,2,2,7,8,9,9,0,0,0,0,0,]
print(data_angka)
print('')
data_user = ['arid','dian','waga','ujang','usep']
print(data_user)
print('')
#####1. menghitung jumlah angka individu
print(f'''
jumlahh angka 5 = {data_angka.count(5)}
jumlahh angka 0 = {data_angka.count(0)}
''')


#####2. mencari nomor index data_user
print(f'''
nomor index dian = {data_user.index('dian')}
nomor index arid = {data_user.index('arid')}
''')
print('')


print('Mengurutkan angka sesuai abjad'.center(60,' '))
#####3. Mengurutkan data_angka & data_user use .sort()
# data_angka.sort()
data_angka.sort()
print(data_angka)
print('')
# data_user.sort()
data_user.sort()
print(data_user)
print('\n\n')


print('Mengebalikan angka setelah di sort'.center(60,' '))
#####4. mengebalikan data menggunakan reverse()
#data_angka.reverse()
data_angka.reverse()
print(data_angka)
#data_user.reverse()
data_user.reverse()
print(data_user)