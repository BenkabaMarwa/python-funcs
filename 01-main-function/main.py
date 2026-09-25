from PyQt5 import QtCore, QtGui, QtWidgets, uic

class school(QtWidgets.QMainWindow):
    def __init__(self):
        super(school,self).__init__()
        uic.loadUi("design.ui",self)
        

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = school()
    window.show()
    sys.exit(app.exec_())

