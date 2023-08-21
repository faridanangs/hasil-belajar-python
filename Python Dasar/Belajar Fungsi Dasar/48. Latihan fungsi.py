# Latihan fungsi

# tampilan proyek
def header():
	print('MARI MENGHITUNG'.rjust(20))
	print('LUAS DAN KELILING SEGITIGA')
	print('\"'*30)

# input user
def input_user():
	lebar = float(input('Lebar ∆: '))
	panjang = float(input('Panjang ∆: '))
	return lebar,panjang

# luas sgitiga
def keliling(lebar,panjang):
	return 2*(lebar+panjang)

# panjang segitiga
def luas(lebar,panjang):
	return lebar*panjang

# display
def display(massage,values):
	print(f'Hasil perhitungan {massage} = {values}')

while True:
	header()
	
	isContinue = input('Mau menghitung atau tdk(y/n)? ')
	if isContinue != 'y':
		if isContinue != 'y' and 'n':
			print('\nuntuk lanjut (y), untuk berhenti(n)\n\n')
		break
		
	isInput = input('menghitung Luas atau Keliling ∆? ')
	if isInput == 'luas':
		LEBAR,PANJANG = input_user()
		LUAS = luas(LEBAR,PANJANG)
		display('luas',LUAS)
		print('\n')
	elif isInput == 'keliling':
		LEBAR,PANJANG = input_user()
		KELILING = keliling(LEBAR,PANJANG)
		display('keliling',KELILING)
		print('\n')
	user = input('Mau lanjut atau nggak(y/n)? ')
	print('\n')
	if user == 'n':
		break
	
	
	
