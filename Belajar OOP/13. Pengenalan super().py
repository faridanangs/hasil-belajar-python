class Hero:
	def __init__(self,name,health,attack):
		self.name = name
		self.health = health
		self.attack = attack
		
	def info(self):
		print('Name Hero\t: {}\n darah\t\t: {}\n kekuatan\t: {}\n'.format(self.name,self.health,self.attack))
		
class Fighter(Hero):
	def __init__(self,name,health,attack):
		super().__init__(name,health,attack)
		super().info()

class Tank(Hero):
		def __init__(self,name,health,attack):
			super().__init__(name,health,attack)
			super().info()
		
hero1 = Fighter('balmond',100,100)
hero2 = Tank('franco',100,50)
