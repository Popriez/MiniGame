import random

class Char(object):
    def __init__(self,name):
        self.name = name
        self.hp = 100
        self.atk = 10
        
    def setName(self,value):
        self.name = value
    def setHp(self,value):
        self.hp = value         
        
    def getHpbar(self):
        count = 1
        self.hpbar = ''
        for count in range(self.hp):
            self.hpbar+='#'
            count+=1   
        return self.hpbar                         
    def getName(self):
        return self.name
    def getHp(self):
        return self.hp
        
class Hero(Char):
    def __init__(self,name):
        super(Hero,self).__init__(name)
        self.spatk = 20
        
class Monster(Char):
    def __init__(self,name):
        super(Monster,self).__init__(name)
        
    def setType(self,value):
        self.type = value
    def setSpatk(self,value):
        if value == 'Boss':
            self.spatk = 30
        else :
            self.spatk = 20

        
        
    def getType(self):
        return self.type
    def getSpatk(self):
        return self.spatk
        
h = Hero('Mickie')
h.setHp(100)

m = Monster('Uvekasasdi')
m.setHp(100)
m.setType('Boss')
m.setSpatk(m.getType())



"""def display():
    print '==================='
    print '        Player'
    print x.name
    print 'HP : %s ' % (x.getHp())
    print 'HP : %s ' % (x.getHpbar())
    print 'ATK : %s ' % (x.atk)
    print 'Special ATK : %s ' % (x.spatk)
    print '=================='


    print '==================='
    print '        Monster'
    print y.name
    print 'Type : %s' % (y.getType())
    print 'HP : %s ' % (y.getHp())
    print 'HP : %s ' % (y.getHpbar())
    print 'ATK : %s ' % (y.atk)
    print 'Speacial ATK : %s ' % (y.getSpatk())
    print '=================='"""


class Game(object):
    def __init__(self):
        self.turn = 00
        
    def randomMonster(self):
        HSP = [0,1,2]
        self.M1 = random.choice(HSP)
    
    def check(self,H1):
        if (H1 == 0 and self.M1 == 1) or (H1 == 1 and self.M1  == 2) or (H1 == 2 and self.M1  == 0):
            m.hp -= h.atk

        elif (H1 == 0 and self.M1 == 2) or (H1 == 1 and self.M1  == 0) or (H1 == 2 and self.M1  == 1):
            h.hp -= m.atk

    
"""def game():
    #display()
    print '\n\n'

    turn = 1
    php = 10
    mhp = 10
    pp=0
    mm=0
    while turn <= 10 :
        HSP = '012'
        M1 = random.choice(HSP)
        P1 = input('\n Enter your 0 or 1 or  2 : \n')
        s = 0
        while (True):
            if P1 != 0 and P1 != 1 and P1 != 2:
                P1 = input("Error! Pls Enter 0 or 1 or 2 : \n")
            else:
                break


        
        if '%s' % (P1) == M1:
            print"\nYou : %s" % (P1)
            print"Monster : %s \n" % (M1)
            print"--- Draw ---"
            display()
            pp=0
            mm=0
        
        
        elif (P1 == 0 and M1 == '1') or (P1 == 1 and M1 == '2') or (P1 == 2 and M1 == '0'):
            print"\nYou : %s" % (P1)
            print"Monster : %s \n" % (M1)
            print"--- Win ---"
            pp+=1
            if pp == 3 :
                mhp-=x.spatk
                print 'You Speacial ATK!!! : %s'%(x.spatk)
            else :
                mhp-=x.atk
                print 'You ATK : %s'%(x.atk)
            y.setHp(mhp)  
            display() 
            mm=0 

        
        
        else:
            print"\nYou : %s" % (P1)
            print"Monster : %s \n" % (M1)
            print"--- Lose ---"
            mm+=1
            if mm == 3 :
                php-=y.getSpatk()
                print '%s Speacial ATK!!! : %s'%(y.name,y.spatk)
            else :
                php-=y.atk
                print '%s ATK : %s'%(y.name,y.atk)  
            x.setHp(php)
            display()
            pp=0
        
        if php == 0:
            print "--- GAME OVER ---"
            break
        elif mhp == 0:
            print "-- VICTORY ---"
            break"""
