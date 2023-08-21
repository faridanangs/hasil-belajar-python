### constructor __init__()
# pengenalan __init__()

class Hero:
	def __init__(self,name,health,power,attack):
		self.name = name
		self.health = health
		self.power = power
		self.attack = attack
hero1 = Hero('atin',100,10,5)
print(hero1.__dict__)