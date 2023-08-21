while True:
	print('')
	print('MASUKAN ANGKA ≤ 7 ATAU ≥ 10')
	print('')
	user = float(input('Masukan Angka: '))
	kurang = user <= 7
	lebih = user >= 10
	hasil = kurang or lebih
	print(hasil)
	print('')
	if hasil == True:
		break
	else:
		pass

user2 = input('Apakah mau coba yg lain (y/n)? ')
print('\n\n')

while True:
	if user2 == 'y':
		print('')
		print('MASUKAN ANGKA ≥ 7 DAN ≤ 10')
		print('')
		user3 = float(input('Masukan angka: '))
		hasil1 = user3 >= 7
		hasil2 = user3 <= 10
		jawaban = hasil1 and hasil2
		print(jawaban)
		if jawaban == True:
			break
		else:
			pass
	elif user2 == 'n':
		break
print('')	
print('Program finish'.center(60,':'))

