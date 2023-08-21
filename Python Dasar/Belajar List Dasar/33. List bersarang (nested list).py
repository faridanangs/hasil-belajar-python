### Nested list/List bersarang

peserta_1 = ['umar',19,'lobar']
peserta_2 = ['ujang',19,'lotim']
peserta_3 = ['askir',19,'loteng']

data_peserta = [peserta_1,peserta_2, peserta_3]
for nama in data_peserta:
	print(f'''
Nama	: {nama[0]}
Usia	: {nama[1]} 
Alamat	: {nama[2]}
''')