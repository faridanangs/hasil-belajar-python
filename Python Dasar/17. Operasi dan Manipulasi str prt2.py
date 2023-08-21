### Method oprator

### 1. upper & lower
nama = 'FArid AnaNg saMudra'

# lower
nama = nama.lower()
print('use lower =',nama)
# upper
nama = nama.upper()
print('use upper =',nama)
print('')


### 2. mengecek str use is method
data = 'HELLO WORLD'

# islower
islower = data.islower()
print('apakah',data,'islower:',str(islower))
# isupper
isupper = data.isupper()
print('apakah',data,'isupper:',str(isupper))
print('')

##### isalpha() ==> di gunakan untuk kengecek huruf
##### isdecimal() ==> di gunakan untuk mengecek angka
##### isalnum() ==> di gunakan untk mngck angka & huruf
##### isspace() ==> di gunakan untk cek spasi,newline,tab
##### istitle() ==>  mengcek huruf kapital di awal kalimat

### 3.mngecek klimat awal use startswith() & endswith()
data = 'ANANG SAMUDRA'
print(data)

data_start = data.startswith('ANANG')
print('Apakah',data[0:5],'awal kalimat?',data_start)
data_end = data.endswith('SAMUDRA')
print('Apakah',data[6:13],'akhir kalimat?',data_end)
print('')

### 4. menggabung & menghapus use split() & join()
data = ['farid','anang','samudra']
print(data)
print('')

## join() > menggabungkan data
data_join = ' - '.join(data)
print(data_join)

## split() > menghapus data
data_split = data_join.split(' - ')#menghapus ' - ' di data_join
print(data_split)
print('')
## replace menggubah klimat yg ada dgan data yg baru
# replace('diganti','mengganti')
nama = 'farid AnaNg saMudra'
print(nama.replace('farid','Wagas'))