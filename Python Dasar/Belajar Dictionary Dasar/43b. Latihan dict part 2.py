# library python
import datetime as dt
import string as str
import random


# template siswa dan data siswa
template_siswa = {
'name' : 'name',
'nis' : '00000000',
'absen' : 0,
'lahir' : dt.datetime(1111,1,11),
}
data_siswa = {}
# akhir template siswa dan data siswa

# title
print(' ~ Data Siswa ~ '.ljust(60,' '))
print('\n')
# akhir title


# while loop dict
while True:
	siswa = dict.fromkeys(template_siswa.keys())
	print('')
	print('ISI DATA BERIKUT')
	print('_________________')
	siswa['name'] = input('Nama siswa: ')
	siswa['nis'] = int(input('Nis siswa: '))
	siswa['absen'] = int(input('No absen: '))
	# lahun lahir
	TAHUN = int(input('Tahun lahir: '))
	BULAN = int(input('Bulan lahir: '))
	TANGGAL = int(input('Tanggal lahir: '))
	siswa['lahir'] = dt.datetime(TAHUN,BULAN,TANGGAL)
		
	# untuk menambah data dict supaya trus ada	
	LEY = ''.join((random.choice(str.ascii_uppercase)for i in range(6)))
	data_siswa.update({LEY:siswa})
	print('\n')
	
	print(f"{'KEY':<7} {'NAME':<20} {'NIS':<13} {'ABSEN':<6} {'LAHIR':<8}")
	print(''.center(60,'`'))
	
	# for loop
	for siswa in data_siswa:	
		KEY = siswa
		NAME = data_siswa[KEY]['name']
		NIS = data_siswa[KEY]['nis']
		ABSEN = data_siswa[KEY]['absen']
		LAHIR = data_siswa[KEY]['lahir'].strftime('%x')
		print(f'{KEY:<7} {NAME:<20} {NIS:<13} {ABSEN:<6} {LAHIR:<8}')
	
	# pilihan lanjut atau gak
	print('\n')		
	lanjut = input('Mau lanjut gak(y/n)? ')
	if lanjut == 'n':
		break
		
print(f'''
___________________________
TERIMAKASIH PROGRAM SELESAI|
````````````````````````````''')
		
