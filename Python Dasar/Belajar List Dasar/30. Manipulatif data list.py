### Manipulasi list

data = ['farid','wagas','raika']


### menambah item pada list sesuai posisi
print('\tSebelum di ubah\n',data)
print('')

##0. mengambil data dari dalam list
print('Mengambil data dari dlm list ke 2 = ',data[2])
print('')

##1. menggubah data list    data[index] = 'kalimat'
data[2] = 'anang'
print(data)

##2.menambah list sesuai keinginan .insert(index,'kalimat')
data.insert(1,'diana')
print(data)

##3. tambh data list di akhir mnggnakan .appen('kalimat')
data.append('hello')
print(data)

##4. hapus data list menggunakan .remove('yg mau d hps')
data.remove('diana')
print(data)

##5. menghapus data list bagian akhir menggnakan   .pop()
data.pop()
print(data)
print('')




####menggabungkan dua buah list menggunakan extend()
data_2 = ['imah','saihu','jodi']
data_2.extend(data)
print('	Sesudah di gabungkan menggunakan extend\n',data_2)
