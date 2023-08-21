### fumgsi dgan parameter/argumen

# def numerik
def numerik(angka1,angka2):
	tambah = angka1 + angka2
	kali = angka1 * angka2
	bagi = angka1 / angka2
	pangkat = angka1 ** angka2
	
	print(f'''def numerik
PERHITUNGAN NUMERIK
hasil {angka1} + {angka2} = {tambah}
hasil {angka1} * {angka2} = {kali}
hasil {angka1} / {angka2} = {bagi:.2f}
hasil {angka1} ** {angka2} = {pangkat:,}
	
	''')
numerik(10,2)
numerik(100,6)

# def input
def user(nama):
	print(f'Hallo {nama} selamat dtng di dunia programming')
user('farid')
print('\n')

# def list
data_list = ['anang','diana','wagas']
def sapa(list):
	print('def list')
	for user in list:
		print('Hello selamat datang',user)
sapa(data_list)
