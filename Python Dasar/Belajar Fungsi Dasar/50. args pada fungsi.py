# *args pada fungsi

def data(*args):
	nama = args[0]
	usia = args[1]
	tinggi = args[2]
	print(f'Nama: {nama} Usia: {usia} Tinggi:{tinggi}')
data('farid anang s',16,175)

def tambah(*data):
	output = 0
	for angka in data:
		output += angka
	return output
print('Jumlah *data:',tambah(1,1,1,1,1,1,1,2,3))