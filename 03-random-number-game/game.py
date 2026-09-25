from PyQt5 import QtCore, QtGui, QtWidgets, uic
import random

class school(QtWidgets.QMainWindow):
    def __init__(self):
        super(school, self).__init__()
        #uic.loadUi("wassim.ui", self)
        self.game()
        

    def game(self):
        y = random.randrange(1000)
        for x in range (1):
            a = int(input("enter a random number"))
            if a==y:
                print("good job")
                break
            elif a<y:
                print("tge number is big")
                
            elif a>y:
                print("number is samal")
                




            









































if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = school()
    window.show()
    sys.exit(app.exec_())

