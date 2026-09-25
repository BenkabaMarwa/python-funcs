from PyQt5 import QtCore, QtGui, QtWidgets, uic
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import sqlite3

database=sqlite3.connect("database.db")
cursor=database.cursor()

class school(QtWidgets.QMainWindow):
    def __init__(self):
        super(school,self).__init__()
        uic.loadUi("design.ui",self)
        self.scrollArea_5WidgetContents = QtWidgets.QWidget(self.scrollArea)
        self.scrollArea.setWidget(self.scrollArea_5WidgetContents)
        self.gridLayout = QGridLayout(self.scrollArea_5WidgetContents)
        self.cardView()




        

    def cardView(self):
        try:
            self.clearLayout(self.gridLayout)
            cursor.execute("SELECT ID, Name, TTCprice, DiscountPrice, PicPath, MaxQuantity, ProfitsPrice FROM Products")
            data = cursor.fetchall()
            self.product_widgets = []

            for x, (id, name, price, dPrice, path, MaxQuantity, Prprice) in enumerate(data):
                frame = QtWidgets.QFrame()
                frame.setMinimumSize(270, 270)
                frame.setMaximumSize(270, 270)
                frame.setStyleSheet("""background-color:#dce4e9;
                                       border-radius: 10px;""")

                layout = QtWidgets.QVBoxLayout(frame)

                label_id = QtWidgets.QLabel(str(id))
                label_id.hide()
                layout.addWidget(label_id)

                label_dPrice = QtWidgets.QLabel(str(dPrice))
                label_dPrice.hide()
                layout.addWidget(label_dPrice)

                label_prPrice = QtWidgets.QLabel(str(Prprice))
                label_prPrice.hide()
                layout.addWidget(label_prPrice)

                label_name = QtWidgets.QLabel(name)
                label_name.setStyleSheet("""font: 75 15pt "MS Shell Dlg 2";
                                        color:#405a78;""")
                label_name.setAlignment(QtCore.Qt.AlignCenter)
                layout.addWidget(label_name)

                pixmap = QtGui.QPixmap(path)
                if not pixmap.isNull():
                    pixmap = pixmap.scaledToWidth(100)
                label_image = QtWidgets.QLabel()
                label_image.setPixmap(pixmap)
                label_image.setAlignment(QtCore.Qt.AlignCenter)
                layout.addWidget(label_image)

                label_price = QtWidgets.QLabel(str(price))
                label_price.setStyleSheet("""font: 75 12pt "MS Shell Dlg 2";
                                         color: red ;""")
                label_price.setAlignment(QtCore.Qt.AlignCenter)
                layout.addWidget(label_price)

                label_maxQuantity = QtWidgets.QLabel(str(MaxQuantity))
                label_maxQuantity.setStyleSheet("""font: 75 10pt "MS Shell Dlg 2";
                                        color:#405a78;""")
                label_maxQuantity.setAlignment(QtCore.Qt.AlignCenter)
                layout.addWidget(label_maxQuantity)

                # Quantity Control Section
                frame2 = QtWidgets.QFrame()
                frame2.setStyleSheet(""" background-color: #dce4e9;;
                                         border: none;
                                         border-radius: 5px; """)
                frame2.setMinimumSize(100, 40)

                layout2 = QtWidgets.QHBoxLayout(frame2)
                layout2.setContentsMargins(5, 5, 5, 5)

                toolButtonMinus = QtWidgets.QToolButton()
                toolButtonMinus.setText("-")
                toolButtonMinus.setIconSize(QtCore.QSize(24, 24))
                toolButtonMinus.setStyleSheet(""" background-color: #405a78;;
                                                  border-radius: 15px;
                                                  color:#dce4e9;; """)
                toolButtonMinus.setMinimumSize(30, 30)
                layout2.addWidget(toolButtonMinus)

                # Store quantity label as an instance attribute
                labelQuantity = QtWidgets.QLabel("0")
                labelQuantity.setAlignment(QtCore.Qt.AlignCenter)
                labelQuantity.setStyleSheet(""" font: 15pt 'MS Shell Dlg 2';
                                                 color: #405a78; """)
                labelQuantity.setMinimumSize(30, 30)
                layout2.addWidget(labelQuantity)

                toolButtonPlus = QtWidgets.QToolButton()
                toolButtonPlus.setText("+")
                toolButtonPlus.setIconSize(QtCore.QSize(24, 24))
                toolButtonPlus.setStyleSheet(""" background-color: #405a78;
                                                 border-radius: 15px;
                                                 color:#dce4e9; """)
                toolButtonPlus.setMinimumSize(30, 30)
                layout2.addWidget(toolButtonPlus)

                layout.addWidget(frame2)
                button = QtWidgets.QPushButton("Ajouter")
                if float(MaxQuantity)<=0.0:
                    toolButtonPlus.setEnabled(False)
                    toolButtonMinus.setEnabled(False)
                    button.setStyleSheet("""background-color: #737373;
                                            color: #dce4e9;
                                            font: 11pt "Rockwell";  """)
                else:
                    button.setStyleSheet("""background-color: #405a78;
                                            color: #dce4e9;;
                                            font: 11pt "Rockwell";  """)
                button.setMinimumSize(30, 30)
                layout.addWidget(button)

                scrollArea=x//3
                self.gridLayout.addWidget(frame,scrollArea,x-3*(scrollArea));

                toolButtonPlus.clicked.connect(lambda _, lbl=labelQuantity: self.increase_quantity(lbl))
                toolButtonMinus.clicked.connect(lambda _, lbl=labelQuantity: self.decrease_quantity(lbl))
                button.clicked.connect(lambda _, lbl_id=label_id, lbl_name=label_name, lbl_price=label_price, lbl_qty=labelQuantity, lbl_prPrice=label_prPrice: 
                                       self.AddProductsPurchased(lbl_id, lbl_name, lbl_price, lbl_qty, lbl_prPrice))

                self.product_widgets.append({
                    "label_id": label_id,
                    "label_name": label_name,
                    "label_price": label_price,
                    "label_quantity": labelQuantity,
                })
                #button.clicked.connect(self.defunct)
        except Exception as error:
            print("CardView", error)

            
    def clearLayout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()
        

if __name__=='__main__':
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = school()
    window.show()
    sys.exit(app.exec_())

