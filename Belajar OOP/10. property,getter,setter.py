#property,getter,setter,deleter
class  Hero:	
	def __init__(self,name,health,power):
		self.__name = name
		self.__health = health
		self.__power = power
	
#Jika menggunakan property hero dapat di update BISA DI UPDATE JIKA INSTANCE VARIABLES BERSIFAT PUBLIK
	#Menggunakan property
	@property
	def info(self):
		return 'Name hero: {}\n  Health: {}\n  Power: {}'.format(self.__name,self.__health,self.__power)
	
#jika ingin mengakses private variables harus di ubah dulu menjadi objek menggunakan property

#property,getter,setter husus power
	@property
	def power(self):
		pass
	#menggunakan getter
	@power.getter
	def power(self):
		return self.__power
	@power.setter
	def power(self,input):
		self.__power = input

#property,getter,setter husus name
	@property
	def name(self):
		pass
	#menggunakan getter
	@name.getter
	def name(self):
		return self.__name
	@name.setter
	def name(self,input):
		self.__name = input

#property,getter,setter husus health
	@property
	def health(self):
		pass
	#mennggunakan getter
	@health.getter
	def health(self):
		return self.__health
	#menggunakan setter
	@health.setter
	def health(self,input):
		self.__health = input

#menghapus health pada hero1
	@health.deleter
	def health(self):
		self.__health = None

#HERO
hero1 = Hero('Usron',100,60)

#mengubah name
print(hero1.__dict__)
hero1.name = 'udin'
print(hero1.__dict__)

#mengubah power
print(hero1.__dict__)
hero1.power = 40
print(hero1.__dict__)

#mengubah health
print(hero1.__dict__)
hero1.health = 9999
print(hero1.__dict__)

#mendelete health
print(hero1.__dict__)
del hero1.health
# del hero1.power error karna belum di @deleter
print(hero1.__dict__)