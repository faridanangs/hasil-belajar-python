# fungsi dgan default argument


# 1. default argument pesan
def argumen(nama,pesan = 'apa kabar'):
	print(f'hai {nama} {pesan}')
argumen('anang')

# 2. default argument numerik
def numerik(x,y=3):
	hasil = x**y
	return hasil
print(numerik(6))

# 3. default argumen mengubah parameter fungsi
def numerik(a,b=6,c=8,d=10):
	return a+b+c+d
print(numerik(127,b=100,c=200))