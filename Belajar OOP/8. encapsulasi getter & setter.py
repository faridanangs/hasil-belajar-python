## encapsulasi
# getter dan setter

class Hero:
	
	def __init__(self,name,health,armor):
#		instance variables private
		self.__name = name
		self.__health = health
		self.__armor = armor
	
	#getter (mengambil variable)
	def getName(self):
		return self.__name
	def getHealth(self):
		return self.__health
	def getArmor(self):
		return self.__armor
	
	#setter (menseting variable)
	def diserang(self,serangan):
		self.__armor -= serangan
	
#Hero	
hero1 = Hero('ucon',100,40)

#game berjalan
print(hero1.getName())
print(hero1.getHealth())

hero1.diserang(30)
print(hero1.getArmor())