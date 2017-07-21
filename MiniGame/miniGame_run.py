### test sys ###
#import getpass
import sys
import getpass
user = getpass.getuser()
#user = getpass.getuser()
path = "C:/Users/"+user+"/Documents/MiniGame"

if not path in sys.path:
    sys.path.append(path)

    
import Create_MiniGame_GUI.miniGameGui as gui


