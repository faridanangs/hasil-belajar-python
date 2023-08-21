# fungsi dengan kembalian (return)

# fungsi pangkat dgan return
def pangkat(x):
	hasil = x**4
	return hasil
y = pangkat(2)
print('Hasil y 2^4 =',y)

# fungsi tambah dgan return
def tambah(x,y):
	return x + y
print('Hasil 2 + 6 =',tambah(2,6))

# fungsi numerik dgan return
def numerik(x,y):
	tambah = x + y
	kali = x * y
	bagi = x / y
	pangkat = x ** y
	return tambah,kali,bagi,pangkat
	
t,k,b,p = numerik(10,6)
print(f'''
hasil tambah  = {t} 
hasil kali = {k}
hasil bagi = {b:.2f} 
hasil pangkat = {p:,}
''')