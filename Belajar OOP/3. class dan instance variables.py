### class dan instance variable

class Hero:   #template
	text = 'farid'#class variable
	num = 0
	def __init__(self,name,health,power,attack):
		#instance variables
		self.name = name
		self.health = health
		self.power = power
		self.attack = attack
		Hero.num += 1
		print(Hero.text,Hero.num)
		print('Nama pada no',Hero.num,'=',name,)
		
hero1 = Hero('atin',100,10,5)
hero2 = Hero('holid',100,10,5)
hero3 = Hero('diana',100,10,5)
