### inheritance

#Template dan supper class
class Hero:
	def __init__(self,name,health):
		self.name = name
		self.health = health
		
#cara melakukan inheritance
# class Hero_warisan(Super_Class)
class Hero_fighter(Hero):
	pass
class Hero_tank(Hero):
	pass
	
hero1 = Hero('Susmus',100)
fighter = Hero_fighter('Argus',79)
tank = Hero_tank('franco',99)

print('Hero Random:',hero1.name)
print('Hero tank:',help(tank))
print('Hero fighter:',fighter.name)