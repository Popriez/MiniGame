#QtGui.QProgressBar

from PySide import QtGui,QtCore
import sys
import random
path = "D:/intern/1907"

if not path in sys.path:
    sys.path.append(path)

    
import Create_MiniGame_GUI.rock_scissor_paper as char
reload(char)
game = char.Game()

class mainWindow(QtGui.QMainWindow):
    
    def __init__(self):
        super(mainWindow, self).__init__()
        self.setWindowTitle('HELLO BUBBLE')
        self.setGeometry(200,200,200,300)
        self.tabMenu()
        self.center = Main()
        self.setCentralWidget(self.center)
        self.connect()
        
    def tabMenu(self):
        self.restart = QtGui.QAction("Restart",self)
        self.exit = QtGui.QAction("Exit",self)

        menubar = self.menuBar()
        fileMenu = menubar.addMenu('manage')
        fileMenu.addAction(self.restart)
        fileMenu.addAction(self.exit)

    def connect(self):
        self.exit.triggered.connect(self.pressexit)
        self.restart.triggered.connect(self.pressrestart)

    def pressexit(self):
        window.close()

    def pressrestart(self):
        reload(char)
        #game = char.Game()
        self.center = Main()
        self.setCentralWidget(self.center)
    
class Main(QtGui.QDialog):
    def __init__(self):
        super(Main,self).__init__()
        self.setFixedSize(QtCore.QSize(500,300))
        self.widget()
        self.layout()
        self.connect()
        
    def widget(self):

        self.mainlabel = QtGui.QLabel("Title Name")

        self.heroHp_label = QtGui.QLabel("HP")
        self.heroHp = char.h.hp
        print self.heroHp
        self.monsterHp_label = QtGui.QLabel("HP")
        self.monsterHp = char.m.hp
        self.heroHp_bar = QtGui.QProgressBar()
        self.heroHp_bar.setValue(self.heroHp)
        self.monsterHp_bar = QtGui.QProgressBar()
        self.monsterHp_bar.setInvertedAppearance (True)
        self.monsterHp_bar.setValue(self.monsterHp)

        self.turn = 0
        self.turn_label = QtGui.QLabel("00")
        
        self.blank = QtGui.QPixmap("blank.png")
        self.rock = QtGui.QPixmap("rock.png")
        self.scissor = QtGui.QPixmap("scissor.png")
        self.paper = QtGui.QPixmap("paper.png")

        self.hero_pic = QtGui.QPixmap("charHero.png")
        self.hero_dis = QtGui.QLabel()
        self.hero_dis.setPixmap (self.hero_pic)
        #self.hero_dis = QtGui.QPushButton("Hero")
        self.hero_card = QtGui.QLabel()
        self.hero_card.setPixmap (self.blank)
        self.vs = QtGui.QLabel("VS")
        self.monster_card = QtGui.QLabel()
        self.monster_card.setPixmap (self.blank)
        self.monster_pic = QtGui.QPixmap("charBoss.png")
        self.monster_dis = QtGui.QLabel()
        self.monster_dis.setPixmap (self.monster_pic)
        
        self.herolabel = QtGui.QLabel("HERO")
        self.monlabel = QtGui.QLabel("MONSTER")

        self.c1_btn = QtGui.QPushButton()
        self.c1_btn.setIcon(QtGui.QIcon("rock.png"))
        self.c1_btn.setFixedSize(QtCore.QSize(100,100))
        self.c1_btn.setIconSize(QtCore.QSize(100,100))
        self.c2_btn = QtGui.QPushButton()
        self.c2_btn.setIcon(QtGui.QIcon("scissor.png"))
        self.c2_btn.setFixedSize(QtCore.QSize(100,100))
        self.c2_btn.setIconSize(QtCore.QSize(100,100))
        self.c3_btn = QtGui.QPushButton()
        self.c3_btn.setIcon(QtGui.QIcon("paper.png"))
        self.c3_btn.setFixedSize(QtCore.QSize(100,100))
        self.c3_btn.setIconSize(QtCore.QSize(100,100))
        
        
    def layout(self):
        mainlayout = QtGui.QVBoxLayout()
        cardlayout = QtGui.QHBoxLayout()
        namelayout = QtGui.QHBoxLayout()
        hplayout = QtGui.QHBoxLayout()
        displaylayout = QtGui.QHBoxLayout()

        mainlayout.addWidget(self.mainlabel)
        self.mainlabel.setAlignment(QtCore.Qt.AlignCenter)

        hplayout.addWidget(self.heroHp_label)
        hplayout.addWidget(self.heroHp_bar)
        hplayout.addWidget(self.turn_label)
        hplayout.addWidget(self.monsterHp_bar)
        hplayout.addWidget(self.monsterHp_label)
        self.monsterHp_bar.setAlignment(QtCore.Qt.AlignCenter)
        self.heroHp_bar.setAlignment(QtCore.Qt.AlignCenter)
        mainlayout.addLayout(hplayout)
        
        displaylayout.addWidget(self.hero_dis)
        displaylayout.addWidget(self.hero_card)
        displaylayout.addWidget(self.vs)
        self.vs.setAlignment(QtCore.Qt.AlignCenter)
        displaylayout.addWidget(self.monster_card)
        displaylayout.addWidget(self.monster_dis)
        mainlayout.addLayout(displaylayout)

        namelayout.addWidget(self.herolabel)
        self.herolabel.setAlignment(QtCore.Qt.AlignLeft)
        namelayout.addWidget(self.monlabel)
        self.monlabel.setAlignment(QtCore.Qt.AlignRight)
        mainlayout.addLayout(namelayout)
        

        cardlayout.addWidget(self.c1_btn)
        cardlayout.addWidget(self.c2_btn)
        cardlayout.addWidget(self.c3_btn)
        mainlayout.addLayout(cardlayout)
        

        #mainlayout.setAlignment(QtCore.Qt.AlignCenter)
        
        
        
        self.setLayout(mainlayout)
        self.setWindowTitle("HELLO BUBBLE")
        
    def connect(self):
        self.c1_btn.clicked.connect(self.pressRock)
        self.c2_btn.clicked.connect(self.pressScissor)
        self.c3_btn.clicked.connect(self.pressPaper)

    def pressRock(self):
        print "Rock"
        game.randomMonster()
        self.H1 = 0
        game.check(self.H1)        
        self.show(self.rock)

    def pressScissor(self):
        print "Scissor"
        game.randomMonster()
        self.H1 = 1
        game.check(self.H1)
        self.show(self.scissor)

    def pressPaper(self):
        print "Paper"
        game.randomMonster()
        self.H1 = 2
        game.check(self.H1)
        self.show(self.paper)

    def show(self,Hinput):

        self.turn += 1
        self.turn_label.setText("%02d"%(self.turn))

        self.hero_card.setPixmap (Hinput)

        if game.M1 == 0:
            self.monster_card.setPixmap (self.rock)
        elif game.M1 == 1:
            self.monster_card.setPixmap (self.scissor)
        elif game.M1 == 2:
            self.monster_card.setPixmap (self.paper)

        self.setHp()


    def setHp(self):
        self.heroHp = char.h.hp
        self.monsterHp = char.m.hp
        self.heroHp_bar.setValue(self.heroHp)
        self.monsterHp_bar.setValue(self.monsterHp)

        if self.monsterHp <= 0:
            win = Victory(self)
            win.show()
        if self.heroHp <= 0:
            lose = Defeted(self)
            lose.show()
        
class Victory(QtGui.QDialog):
    def __init__(self,parent):
        super(Victory,self).__init__(parent)
        self.setFixedSize(QtCore.QSize(300,200))
        self.widget()
        self.layout()
        self.connect()
        
    def widget(self):

        self.mainlabel = QtGui.QLabel("YOU WIN")

        self.hero_pic = QtGui.QPixmap("charHero.png")
        self.hero_dis = QtGui.QLabel()
        self.hero_dis.setPixmap (self.hero_pic)

        self.OK_btn = QtGui.QPushButton("OK")
        
    def layout(self):
        mainlayout = QtGui.QVBoxLayout()
        suplayout = QtGui.QHBoxLayout()

        suplayout.addWidget(self.hero_dis)
        suplayout.addWidget(self.mainlabel)
        mainlayout.addLayout(suplayout)

        mainlayout.addWidget(self.OK_btn)

        self.setLayout(mainlayout)
        self.setWindowTitle("WIN")
        
    def connect(self):
        self.OK_btn.clicked.connect(self.exit)

    def exit(self):
        window.close()

class Defeted(QtGui.QDialog):
    def __init__(self,parent):
        super(Defeted,self).__init__(parent)
        self.setFixedSize(QtCore.QSize(300,200))
        self.widget()
        self.layout()
        self.connect()
        
    def widget(self):

        self.mainlabel = QtGui.QLabel("YOU LOSE")

        self.monster_pic = QtGui.QPixmap("charBoss.png")
        self.monster_dis = QtGui.QLabel()
        self.monster_dis.setPixmap (self.monster_pic)

        self.OK_btn = QtGui.QPushButton("OK")
        
    def layout(self):
        mainlayout = QtGui.QVBoxLayout()
        suplayout = QtGui.QHBoxLayout()

        suplayout.addWidget(self.monster_dis)
        suplayout.addWidget(self.mainlabel)
        mainlayout.addLayout(suplayout)

        mainlayout.addWidget(self.OK_btn)

        self.setLayout(mainlayout)
        self.setWindowTitle("LOSE")
        
    def connect(self):
        self.OK_btn.clicked.connect(self.exit)

    def exit(self):
        window.close()


app = QtGui.QApplication(sys.argv)
window = mainWindow()
window.show()
app.exec_()