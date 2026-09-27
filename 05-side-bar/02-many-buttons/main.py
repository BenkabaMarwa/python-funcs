from PyQt5 import QtCore, QtGui, QtWidgets, uic

class school(QtWidgets.QMainWindow):
    def __init__(self):
        super(school,self).__init__()
        uic.loadUi("design.ui",self)
        self.Home()
        
        self.HomeButton.clicked.connect(self.Home)
        self.ManagementButton.clicked.connect(self.Management)
        self.ProductButton.clicked.connect(self.Products)
        self.ClientButton.clicked.connect(self.Clients)
        self.WorkerButton.clicked.connect(self.Workers)
        self.SupplierButton.clicked.connect(self.Suppliers)
        self.RequestButton.clicked.connect(self.Debts)
        self.PaymentButton.clicked.connect(self.Payment)
        self.ReportButton.clicked.connect(self.Reports)
        self.SettingButton.clicked.connect(self.Setting)
        


    #MenuStart
    def Home(self):
        #self.stackedWidget.setCurrentIndex(18)
        self.HomeFrame.setStyleSheet("background-color:#e2e9ed")
        self.HomeButton.setStyleSheet("color:#405a78; font: 9pt 'Rockwell';")
        self.HometoolButton.hide()
        self.HometoolButton2.show()
        self.OldManagement()
        self.OldProducts()
        self.OldClients()
        self.OldWorkers()
        self.OldSuppliers()
        self.OldDebts()
        self.OldPayment()
        self.OldReports()
        self.OldSetting()
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
            self.OldProducts()
            self.OldClients()
            self.OldWorkers()
            self.OldSuppliers()
            self.OldDebts()
            self.OldPayment()
            self.OldReports()
            self.OldSetting()
        except Exception as e:
            print(e)
    def OldManagement(self):
        self.ManagementFrame.setStyleSheet("background-color:#405a78")
        self.ManagementButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell';")
        self.ManagementtoolButton.show()
        self.ManagementtoolButton2.hide()

    def Products(self):
        #self.stackedWidget.setCurrentIndex(5)
        self.Productframe.setStyleSheet("background-color:#e2e9ed")
        self.ProductButton.setStyleSheet("color:#405a78; font: 9pt 'Rockwell';")
        self.ProducttoolButton.hide()
        self.ProducttoolButton2.show()
        self.OldHome()
        self.OldManagement()
        self.OldClients()
        self.OldWorkers()
        self.OldSuppliers()
        self.OldDebts()
        self.OldPayment()
        self.OldReports()
        self.OldSetting()
    def OldProducts(self):
        self.Productframe.setStyleSheet("background-color:#405a78")
        self.ProductButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell';")
        self.ProducttoolButton.show()
        self.ProducttoolButton2.hide()

    def Clients(self):
        #self.stackedWidget.setCurrentIndex(6)
        self.Clientframe.setStyleSheet("background-color:#e2e9ed")
        self.ClientButton.setStyleSheet("color:#405a78; font: 9pt 'Rockwell'")
        self.ClienttoolButton.hide()
        self.ClienttoolButton2.show()
        self.OldHome()
        self.OldManagement()
        self.OldProducts()
        self.OldWorkers()
        self.OldSuppliers()
        self.OldDebts()
        self.OldPayment()
        self.OldReports()
        self.OldSetting()
    def OldClients(self):
        self.Clientframe.setStyleSheet("background-color:#405a78")
        self.ClientButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell';")
        self.ClienttoolButton.show()
        self.ClienttoolButton2.hide()

    def Workers(self):
        #self.stackedWidget.setCurrentIndex(7)
        self.Workerframe.setStyleSheet("background-color:#e2e9ed")
        self.WorkerButton.setStyleSheet("color:#405a78; font: 9pt 'Rockwell'")
        self.WorkertoolButton.hide()
        self.WorkertoolButton2.show()
        self.OldHome()
        self.OldManagement()
        self.OldProducts()
        self.OldClients()
        self.OldSuppliers()
        self.OldDebts()
        self.OldPayment()
        self.OldReports()
        self.OldSetting()
    def OldWorkers(self):
        self.Workerframe.setStyleSheet("background-color:#405a78")
        self.WorkerButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell'")
        self.WorkertoolButton.show()
        self.WorkertoolButton2.hide()

    def Suppliers(self):
        #self.stackedWidget.setCurrentIndex(8)
        self.Supplierframe.setStyleSheet("background-color:#e2e9ed")
        self.SupplierButton.setStyleSheet("color: #405a78; font: 9pt 'Rockwell'")
        self.SuppliertoolButton.hide()
        self.SuppliertoolButton2.show()
        self.OldHome()
        self.OldManagement()
        self.OldProducts()
        self.OldClients()
        self.OldWorkers()
        self.OldDebts()
        self.OldPayment()
        self.OldReports()
        self.OldSetting()
    def OldSuppliers(self):
        self.Supplierframe.setStyleSheet("background-color:#405a78")
        self.SupplierButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell'")
        self.SuppliertoolButton.show()
        self.SuppliertoolButton2.hide()

    def Payment(self):
        #self.stackedWidget.setCurrentIndex(11)
        self.Paymentframe.setStyleSheet("background-color:#e2e9ed")
        self.PaymentButton.setStyleSheet("color: #405a78; font: 9pt 'Rockwell';")
        self.PaymenttoolButton.hide()
        self.PaymenttoolButton2.show()
        self.OldHome()
        self.OldManagement()
        self.OldProducts()
        self.OldClients()
        self.OldWorkers()
        self.OldSuppliers()
        self.OldDebts()
        self.OldReports()
        self.OldSetting()
    def OldPayment(self):
        self.Paymentframe.setStyleSheet("background-color:#405a78")
        self.PaymentButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell';")
        self.PaymenttoolButton.show()
        self.PaymenttoolButton2.hide()

    def Reports(self):
        #self.stackedWidget.setCurrentIndex(12)
        self.Reportframe.setStyleSheet("background-color:#e2e9ed")
        self.ReportButton.setStyleSheet("color: #405a78; font: 9pt 'Rockwell';")
        self.ReporttoolButton.hide()
        self.ReporttoolButton2.show()
        self.OldHome()
        self.OldManagement()
        self.OldProducts()
        self.OldClients()
        self.OldWorkers()
        self.OldSuppliers()
        self.OldDebts()
        self.OldPayment()
        self.OldSetting()
    def OldReports(self):
        self.Reportframe.setStyleSheet("background-color:#405a78")
        self.ReportButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell';")
        self.ReporttoolButton.show()
        self.ReporttoolButton2.hide()

    def Debts(self):
        #self.stackedWidget.setCurrentIndex(14)
        self.Requestframe.setStyleSheet("background-color:#e2e9ed")
        self.RequestButton.setStyleSheet("color: #405a78; font: 9pt 'Rockwell';")
        self.RequesttoolButton.hide()
        self.RequesttoolButton2.show()
        self.OldHome()
        self.OldManagement()
        self.OldProducts()
        self.OldClients()
        self.OldWorkers()
        self.OldSuppliers()
        self.OldPayment()
        self.OldReports()
        self.OldSetting()
    def OldDebts(self):
        self.Requestframe.setStyleSheet("background-color:#405a78")
        self.RequestButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell';")
        self.RequesttoolButton.show()
        self.RequesttoolButton2.hide()
        
    def Setting(self):
        #self.stackedWidget.setCurrentIndex(19)
        self.Settingframe.setStyleSheet("background-color:#e2e9ed")
        self.SettingButton.setStyleSheet("color: #405a78; font: 9pt 'Rockwell';")
        self.SettingtoolButton.hide()
        self.SettingtoolButton2.show()
        self.OldHome()
        self.OldManagement()
        self.OldProducts()
        self.OldClients()
        self.OldWorkers()
        self.OldSuppliers()
        self.OldPayment()
        self.OldReports()
        self.OldDebts()
    def OldSetting(self):
        self.Settingframe.setStyleSheet("background-color:#405a78")
        self.SettingButton.setStyleSheet("color:#e2e9ed; font: 9pt 'Rockwell';")
        self.SettingtoolButton.show()
        self.SettingtoolButton2.hide()







if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = school()
    window.show()
    sys.exit(app.exec_())

