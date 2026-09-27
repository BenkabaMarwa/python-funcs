from PyQt5 import QtCore, QtGui, QtWidgets, uic

class school(QtWidgets.QMainWindow):
    def __init__(self):
        super(school,self).__init__()
        uic.loadUi("design.ui",self)
        self.Home()
        
        self.HomeButton.clicked.connect(self.Home)
        self.ManagementButton.clicked.connect(self.Management)
    
        


    #MenuStart
    def Home(self):
        #self.stackedWidget.setCurrentIndex(18)
        self.HomeFrame.setStyleSheet("background-color:#e2e9ed")
        self.HomeButton.setStyleSheet("color:#405a78; font: 9pt 'Rockwell';")
        self.HometoolButton.hide()
        self.HometoolButton2.show()
        self.OldManagement()
        
    def OldHome(self):
        self.HomeFrame.setStyleSheet("background-color:#405a78")
        self.HomeButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell';")
        self.HometoolButton.show()
        self.HometoolButton2.hide()


    def Management(self):
        try:
            #self.stackedWidget.setCurrentIndex(1)
            self.ManagementFrame.setStyleSheet("background-color:#e2e9ed")
            self.ManagementButton.setStyleSheet("color: #405a78; font: 9pt 'Rockwell';")
            self.ManagementtoolButton.hide()
            self.ManagementtoolButton2.show()
            self.OldHome()
            
        except Exception as e:
            print(e)
    def OldManagement(self):
        self.ManagementFrame.setStyleSheet("background-color:#405a78")
        self.ManagementButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell';")
        self.ManagementtoolButton.show()
        self.ManagementtoolButton2.hide()













    



if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = school()
    window.show()
    sys.exit(app.exec_())

