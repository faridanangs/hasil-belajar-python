### Magic method

class Buah:
	
#yang terpenting adalah method __init__
	def __init__(self,name,jumlah):
		self.name = name
		self.jumlah = jumlah
		
	###if want  repr ikut di pnggl kita hrs mnruh repr di print
	#magic method __repr__
	def __repr__(self):
		return 'repr Ini adalah buah: {}, berjumlah: {}'.format(
		self.name,
		self.jumlah
		)
	
	#__str__ lebih di dahulukan di print dari yang lain
	#magic method __str__
	def __str__(self):
		return 'str ini adalah buah: {}, berjumlah: {}'.format(
		self.name,
		self.jumlah
		)
	
	##harus di add argumen >1  spya nisa dijlnkan	
	#magic method __add__ cocok untuk oprsi mtk
	def __add__(self,input):
		return self.jumlah + input.jumlah
		
buah1 = Buah('Durian',10)
buah2 = Buah('Rambutan',50)

print(repr(buah1))
print(buah1)
print(f'10buah + 50buah = ',buah1 + buah2,'buah')