# membaca file external menggunakan with
with open('file.txt','r') as file:
	print('Apakah ini bisa di baca?',file.readable())
#	print('Apakah ini bisa di tulis?',file.writable())
	print('\n')
#	print('Membaca text per line:',file.readline())
#	print('Membaca text bersama list:',file.readlines())
	print(file.read())
print('Apakah ini sudah di tutup?',file.closed)