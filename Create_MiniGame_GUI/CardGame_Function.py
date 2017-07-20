import random
class Character(object):
    def __init__(self,name):
        self.name = name
        self.hp = 0
        self.atk = 0
        self.deff = 0 
        self.brk = 0
        self.hel = 0
        self.selectCard = 0

        
                
class Hero(Character):
    
   def __init__(self,name):
       super(Hero,self).__init__(name)
       self.hp = 300
       self.atk = 50
       self.deff = 30
       self.brk = 70
       self.hel = 30
       
class Monster(Character):
    
   def __init__(self,name):
       super(Monster,self).__init__(name)
       if self.name == 'Boss':
           self.hp = 300
           self.atk = 40
           self.deff = 30
           self.brk = 50
           self.hel = 30
       else :
           self.hp = 150
           self.atk = 30
           self.deff = 20
           self.brk = 40
           self.hel = 30

'''       
class Boss(Character):
    
   def __init__(self,name):
       super(Boss,self).__init__(name)
       self.hp = 300
       self.atk = 40
       self.deff = 30
       self.brk = 50
       self.hel = 30
'''       
   
class CardGame(object):
    def __init__(self,Hero,Monster,Boss):
        super(CardGame,self).__init__()
        self.hero = Hero
        self.monster = Monster
        self.boss = Boss
        self.cardHero = [0,0,0]
         
    
    def randomCard(self,x):
        x.selectCard = random.randint(0,3)
    
    def randomCardHero(self):
        for x in range(3):
            self.cardHero[x] = random.randint(0,3)
        print 'Draw Card : ' + str(self.cardHero)
        
    def chooseCard(self):
        print 'You Have Card ' + str(self.cardHero)
        while True:
            self.hero.selectCard = input('Hero SelectCard')
            if self.hero.selectCard == self.cardHero[0]:
                self.cardHero[0]=self.cardHero[1]
                self.cardHero[1]=self.cardHero[2]
                break
            elif self.hero.selectCard == self.cardHero[1]:
                self.cardHero[1]=self.cardHero[2]
                break
            elif self.hero.selectCard == self.cardHero[2]:
                break
            else :
                print 'Mistake Choose pls try Again'
                
        
    
    def action(self):
        self.state = 1
        self.fineMonster = 1
        self.randomCardHero()
        self.monsterType = self.monster 
        while self.state != 3 :
            self.turn = 1
            while self.hero.hp >0 and self.monsterType.hp >0 :
                print '--------- Turn ' + str(self.turn) +' -------------'
                self.randomCard(self.monsterType)       
                self.chooseCard()
                print 'Hero SelectCard == ' + str(self.hero.selectCard) + '\nMonster SelectCard == ' + str(self.monsterType.selectCard)
                if self.hero.selectCard == 0 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= self.monsterType.atk
                    self.monsterType.hp -= self.hero.atk
                    print 'Hero Attack : ' +str(self.hero.atk)
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk)
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 1 :
                    self.monsterType.hp -= (self.hero.atk - self.monsterType.deff)
                    print 'Hero Attack : ' +str(self.hero.atk)
                    print self.monsterType.name + ' Deffend : ' +str(self.monsterType.deff)
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 2 :
                    self.monsterType.hp -= self.hero.atk
                    print 'Hero Attack : ' + str(self.hero.atk)
                    print self.monsterType.name + ' Break  : Break Fail '
                elif self.hero.selectCard == 0 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp -= (self.hero.atk-self.monsterType.hel)
                    print 'Hero Attack : ' +str(self.hero.atk)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= ( self.monsterType.atk - self.hero.deff )
                    print 'Hero Deffend : ' +str(self.hero.deff)
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk)            
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 1 :
                    print 'Hero Deffend : ' +str(self.hero.deff)
                    print self.monsterType.name + ' Deffend : ' +str(self.monsterType.deff)   
                    print 'Nothing'
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= self.monsterType.brk
                    print 'Hero Deffend : Deffend Fail'
                    print self.monsterType.name + ' Break : ' +str(self.monsterType.brk)  
                elif self.hero.selectCard == 1 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp += self.monsterType.hel
                    print 'Hero Deffend : ' +str(self.hero.deff)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)  
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= self.monsterType.atk
                    print 'Hero Break : Break Fail' 
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk) 
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 1 :
                    self.monsterType.hp -= self.hero.brk
                    print 'Hero Break : ' +str(self.hero.brk)
                    print self.monsterType.name + ' Deffend : Deffend Fail'
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= self.monsterType.brk
                    self.monsterType.hp -= self.hero.brk
                    print 'Hero Break : ' +str(self.hero.brk)
                    print self.monsterType.name + ' Break : ' +str(self.monsterType.brk)
                elif self.hero.selectCard == 2 and self.monsterType.selectCard == 3 :
                    self.monsterType.hp -= (self.hero.brk-self.monsterType.hel)
                    print 'Hero Break : ' +str(self.hero.brk)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 0 :
                    self.hero.hp -= (self.monsterType.atk-self.hero.hel)
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Attack : ' +str(self.monsterType.atk)
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 1 :
                    self.hero.hp += self.hero.hel
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Deffend '
                elif self.hero.selectCard == 3 and self.monsterType.selectCard == 2 :
                    self.hero.hp -= (self.monsterType.brk-self.hero.hel)
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Break : ' +str(self.monsterType.brk)
                elif self.hero.selectCard == 3 and self.monster.selectCard == 3 :
                    self.monsterType.hp += self.monsterType.hel
                    self.hero.hp += self.hero.hel
                    print 'Hero Heal : ' +str(self.hero.hel)
                    print self.monsterType.name + ' Heal : ' +str(self.monsterType.hel)
                    
                if self.hero.hp > 300 :
                    self.hero.hp = 300
                if self.monster.hp > 150 :
                    self.monsterType.hp = 150
                if self.boss.hp > 300 :
                    self.boss.hp = 300
                print self.hero.name + ' HP : ' + str(self.hero.hp)
                print self.monsterType.name + '  HP : ' + str(self.monsterType.hp)
                self.turn+=1
                
                self.cardHero[2] = random.randint(0,3)
                                
            if self.state == 1 :
                if self.hero.hp <= 0 :
                    print '-------- Monster Win -----------'
                    break
                else :
                    self.state+=1
                    print '-------- Hero Win --------------'
                    print '-------- Next State (Boss) ----------'
                    self.monsterType = self.boss
                    continue
                    
            elif self.state == 2 :
                if self.hero.hp <= 0 :
                    print '-------- Boss Win -----------'
                else :
                    print '-------- Hero Win --------------'
                
                print '--------- End Game ----------'
                break
            

        
              


       
x= Hero('Hero')
y= Monster('Monster')
z= Monster('Boss')
c= CardGame(x,y,z)
c.action()





