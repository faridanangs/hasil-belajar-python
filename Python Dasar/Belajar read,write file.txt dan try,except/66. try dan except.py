## penggunakan try dan except

'''
# contoh penggunakan pada aplikasi
while True:
	user = int(input('Masukan angka pembagi: '))
	try:
		hasil = 0
		hasil = 10/user
		print(hasil)
		isDone = input('Apakah mau lanjut(y/n)? ')
		if isDone == 'n':
			break		
	except:
		print('Pembagi tdk boleh 0')		
print('\nProgram selesai')

'''
'''
# contoh penggunaan pada membuat,membaca,dan menulis file.txt

while True:
	try:
		with open('filetryexcept2.txt','r') as file:
			print(file.read())
		break
		
	except:
		print('Data filetryexcept2.txt tdk ada  datanya')
		print('Saya akan membuatnya sekarang')
		with open('filetryexcept2.txt','w',encoding='utf-8') as file:
			file.write('Data sudah di buat tuan muda\n')
		with open('filetryexcept.txt','a') as file:
			file.write('Data sudah di buat tuanku')
		
print('\n\n')

'''
'''
from numbers import Number

def tambah(a,b):
	if not isinstance(a,Number) or not isinstance(b,Number):
		raise 'INPUT HARUS ANGKA'
	return a+b
print('Hasil tambah = ',tambah(2,3))

'''
## Cara untuk menampilkan error
user = int(input('Masukan angka pembagi: '))
try:
	hasil = 10/user
	print(hasil)	
## cara 1
#except Exception as error:
#	print(error)
## cara 2
except ZeroDivisionError as error:
	print(error)


	