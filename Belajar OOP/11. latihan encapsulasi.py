class Hero:
	def __init__(self,nama,darah,serang,pelindung):
		self.__nama = nama
		self.__darahAwal = darah
		self.__serangAwal = serang
		self.__pelindungAwal = pelindung
		self.__level = 1
		self.__exp = 0
		
		self.__darahMax = self.__darahAwal * self.__level
		self.__serangMax = self.__serangAwal * self.__level
		self.__pelindungMax = self.__pelindungAwal * self.__level
		self.__darah = self.__darahMax
		
	@property
	def info(self):
		return '''Nama Hero\t: {}
 Level Hero\t: {}
 Darah Hero\t: {}/{}
 Serangan\t: {}
 Pelindung\t: {}
'''.format(self.__nama,self.__level,self.__darah,self.__darahMax,self.__serangMax,self.__pelindungMax)
	
	@property
	def gainExp(self):
		pass
	
	@gainExp.setter
	def gainExp(self,inputUser):
		self.__exp += inputUser
		if (self.__exp >= 100):
			self.__level += 1
			self.__exp -= 100
			self.__darahMax = self.__darahAwal * self.__level
			self.__serangMax = self.__serangAwal * self.__level
			self.__pelindungMax = self.__pelindungAwal * self.__level
			
			
	def attack(self,lawan):
			self.gainExp = 75

hero1 = Hero('Uskan',100,25,20)
hero2 = Hero('Kisan',100,55,13)

hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
hero1.attack(hero2)
print(hero1.info)