import datetime as dt

data_siswa1 = {
'name' : 'ujang',
'nis' : 1021213382,
'sks' : 35,
'lahir' : dt.datetime(2006,5,31)
}
data_siswa2 = {
'name' : 'ujanang',
'nis' : 1021213382,
'sks' : 35,
'lahir' : dt.datetime(2076,5,31)
}
data_siswa3 = {
'name' : 'ujasjaiang',
'nis' : 1021213382,
'sks' : 35,
'lahir' : dt.datetime(2012,5,31)
}

data = {
'uhuy':data_siswa1,
'ulala':data_siswa2,
'ukek':data_siswa3,
}

print(f'{"KEY":<7} {"NAME":<20} {"NIS":<13} {"SKS":<6} {"LAHIR":<8}')
print(''.center(60,"\'"))
for siswa in data.keys():
	KEY = siswa
	NAME = data[KEY]['name']
	NIS = data[KEY]['nis']
	SKS = data[KEY]['sks']
	LAHIR = data[KEY]['lahir'].strftime('%x')
	
	print(f'{KEY:<7} {NAME:<20} {NIS:<13} {SKS:<6} {LAHIR:<8}')
	