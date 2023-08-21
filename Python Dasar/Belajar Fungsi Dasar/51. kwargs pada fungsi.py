# **kwargs pada fungsi

# semua harus sama jika di ubah satu maka semua harus di ubah
def fungsi(**kwargs):
	nusma = kwargs['nusma']
	tinggi = kwargs['tinggi']
	usia = kwargs['usia']
	print(f'Nama = {nusma}, Tinggi = {tinggi}, Usia = {usia}')
	
fungsi(nusma='anang',tinggi=175,usia=16)

# numerik *args & **kwargs
def numerik(*args,**kwargs):
	if kwargs['option'] == 'tambah':
		output = 0
		for angka in args:
			output += angka
	if kwargs['option'] == 'kali':
		output = 1
		for angka in args:
			output *= angka
	return output


print('Hasil tambah =',numerik(1,2,3,4,option='tambah'))
print('Hasil kali =',numerik(1,2,3,4,option='kali'))