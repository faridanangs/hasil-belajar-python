data_list = []

print('MASUKAN DATA SISWA'.center(60,'!'))
print('')
while True:
	siswa = input('Nama siswa\t: ')
	upper_siswa = siswa.upper()
	
	
	gender = input('Keterangan\t: ')
	upper_gender = gender.upper()
	
	data_siswa = [upper_siswa,upper_gender]
	
	data_list.append(data_siswa)
	print('\n\n')
	print(''.center(60,'|'))
	for index,data in enumerate(data_list):
		print(f'{index +1}: Nama Siswa:{data[0]}\tKeterangan:{data[1]}')
	print(''.center(60,'|'))	
	user = input('Mau lanjut gak(y/n)? ')
	print('')
	if user == 'n':
		break
	
	