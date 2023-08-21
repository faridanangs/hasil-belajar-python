import datetime as dt

template_siswa = {
'name' : 'name',
'nis' : '00000000',
'absen' : 0,
'lahir' : dt.datetime(1111,1,11),
}

print(' ~ Data Siswa ~ '.center(60,' '))
print('\n\n')

siswa = dict.fromkeys(template_siswa.keys())

siswa['name'] = input('Nama siswa: ')
siswa['nis'] = int(input('Nis siswa: '))
siswa['absen'] = int(input('No absen: '))
# lahun lahir
TAHUN = int(input('Tahun lahir: '))
BULAN = int(input('Bulan lahir: '))
TANGGAL = int(input('Tanggal lahir: '))
siswa['lahir'] = (TAHUN,BULAN,TANGGAL)

print(siswa)
