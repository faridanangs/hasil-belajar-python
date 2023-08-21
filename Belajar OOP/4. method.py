## Method

# template class
class Hero:
	#class variable
	jumlah_hero = 0
	
	def __init__(self,name,health,attack):
		#instance variables
		self.name = name
		self.health = health
		self.attack = attack
		Hero.jumlah_hero += 1
		
	#method tanpa return dan argumen
	def sapa(se): #=> jika self tdk ada program error
		print('Halo',se.name,'Apakabar? saya harap baik',)
	
	#method menggunakan argumen tanpa teturn
	def healthUp(self,up):
		self.health += up
	
	#method menggunakan return
	def getHero(ok): #==> ok must same with at under
		return ok.name,ok.health
	
# <Hero>
hero1 = Hero('udin',100,50)
hero2 = Hero('ucup',100,35)
hero3 = Hero('ruslan',100,48)
#<Hero/>

# method sapa
hero1.sapa()
#method menambah darah/ healtUp
hero1.healthUp(10)
#method mendaoatkan info hero/getHero
print(hero1.getHero())


