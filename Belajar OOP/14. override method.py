class Hero:
	def __init__(self,name,health):
		self.name = name
		self.health = health
		
	def info(self):
		print('{} health: {}'.format(self.name,self.health))


class Fighter(Hero):
	def __init__(self,name,health):
		super().__init__(name,health)
	#override
	def info(self):
		print('\n{} health: {}\n type: fighter\n'.format(self.name,self.health))
		

class Tank(Hero):
	def __init__(self,name,health):
		super().__init__(name,health)
	# override
	def info(self):
		print('\n{} health: {}\n type: tank\n'.format(self.name,self.health))
		
#Hero
hero1 = Fighter('Balmond',100)
hero2 = Hero('Franco',200) # Hero() dia akan mengeprin yang ada di dalam hero atau memproritaskan subclassnya
hero1.info()
hero2.info()