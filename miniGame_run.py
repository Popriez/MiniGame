### test sys ###
#import getpass
import sys
#user = getpass.getuser()
path = "D:/intern/1907"

if not path in sys.path:
    sys.path.append(path)

    
import Create_MiniGame_GUI.miniGameGui as gui

reload(gui)

