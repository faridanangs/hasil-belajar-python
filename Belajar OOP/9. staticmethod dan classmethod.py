##Belajar staticmethod dan classmethod


class Hero:
	#variable private
	__jumlahHero = 0
	
	def __init__(self,name):
		self.__name = name
		Hero.__jumlahHero += 1

	# method ini hanya berlaku untuk objek
	def getJumlah1(self):
		return Hero.__jumlahHero
	# tdk berlaku untuk objek dan berlaku untuk class
	def getJumlah2():
		return Hero.__jumlahHero
	
	
### method ini berlaku untuk objek dan class
	@staticmethod
	def getStatic1():
		return Hero.__jumlahHero

		
### Menggunakan classmethod supaya program tdk error ketika class di ubah dan berlaku untuk objek dan class
	@classmethod
	def getClass1(cls):
		return cls.__jumlahHero


# Heroo
hero1 = Hero('Ucok')
hero2 = Hero('Usman')
hero1 = Hero('Fulan')
hero2 = Hero('Alibaba')

"""
TIDAK MENGGUNAKAN staticmethod & classmethod
# print(Hero.getJumlah()) ==> error
print(Hero.getJumlah2()) # Tdk error krna () kosong
"""
### MENGGUNAKAN staticmethod
print(hero1.getStatic1())
print(Hero.getStatic1())

### MENGGUNAKAN classmethod
print(hero1.getClass1())
print(Hero.getClass1())