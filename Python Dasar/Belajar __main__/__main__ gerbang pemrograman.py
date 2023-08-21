
# nilai __name__ akan berubah menjadi __main__ dikarnakan __name__ di jalankan di file utama/internal
print(f'Nilai __name__ pada gerbang pemrograman: {__name__}')
print('')

# nilai __name__ dari file external,percobaan setelah di import ke file gerbang pemrograman akan berubah menjadi name file nya
import Percobaan
print('\n')

# contoh penggunaan __main__
# deklarasi
def tambah(x,y):
	return x+y
# fungsi utama
if __name__ =='__main__':
	x = 110
	y = 2
	hasil = tambah(x,y)
	print('Hasil tambah =',hasil)