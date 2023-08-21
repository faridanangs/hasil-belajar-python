### Latihan oop

class Hero:
	jumlah_hero = 0
	def __init__(self,name,health,attack,armor):
		self.name = name
		self.health = health
		self.attack = attack
		self.armor = armor
		Hero.jumlah_hero += 1
	
	def serang(self,lawan):
		print(self.name,'menyerang',lawan.name)
		lawan.diserang(self,self.attack)
		
	def diserang(self,lawan,attack_diterima):
		print(self.name,'diserang',lawan.name)
		serangan = attack_diterima / self.armor
		print('Serangan',lawan.name,'terasa',serangan)
		self.health -= serangan
		print('Sisa darah',self.name,'adalah',self.health)
		
		self.mati(lawan)
		print('\n')
		
	def mati(self,lawan):
		if self.health <= 0:
			print('\n\n')
			print(self.name,'Sudah Mati')
			
		
hero1 = Hero('ujang',100,50,20)
hero2 = Hero('usman',100,60,10)

hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)
hero1.serang(hero2)