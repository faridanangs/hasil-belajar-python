# multiple inheritance

#class tipe
class Type:
	def tipe(self,tipe):
		self.tipe = tipe
	def showTipe(self):
		print('Tipe:',self.tipe)
	
#class team
class Team:
	def team(self,team):
		self.team = team
	def showTeam(self):
		print('Team:',self.team)
	
#class multiple inheritance
class Hero(Type,Team):
	def __init__(self,name,health):
		self.name = name
		self.health = health
	def showInfo(self):
		return '{} health: {}'.format(self.name,self.health)
		
hero1 = Hero('Usman',100)
print(hero1.showInfo())

hero1.team('Ucup')
hero1.showTeam()

hero1.tipe('Fighter')
hero1.showTipe()