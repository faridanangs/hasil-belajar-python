### Oprasi numerik

# Tambah
def tambah(*args):
	hasil = 0
	for angka in args:
		hasil += angka
	return hasil
# Kali
def kali(*args):
	hasil = 1
	for angka in args:
		hasil *= angka
	return hasil
# Pangkat
def pangkat(n):
	return lambda x:x**n
	