###  Oprasi dictionary


data_dict = {
'na' : 'diana milda',
'gn' : 'gunandi',
'gs' : 'gas elpiji',
}
print(data_dict)
print('\n\n')


##1. menghitung data dict
jumlah = len(data_dict)
print('Jumlah data dict =',jumlah)
print('\n')

##2. mengecek apakah data dict ada atau tidak
cek = 'ung' in data_dict
print('Apakah ung ada di data_dict?',cek)
print('\n')

##3. mengakses value atau membaca menggunakan get()
print('key dict gs =',data_dict.get('gs'))
print(data_dict.get('ls','maaf key ls yg tuan mskn tdk ada'))
print('\n')

##4.update dan menambah data dictionary use update({})
data_dict.update({'gs':'wagas'})
data_dict.update({'ng':'anang'})
print(data_dict)
print('\n')

##5. mendelete data dictionary use del data_dict[' ']
del data_dict['ng']
print(data_dict)