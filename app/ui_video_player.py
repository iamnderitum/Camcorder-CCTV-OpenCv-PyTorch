from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        
        Dialog.setObjectName('Dialog')
        Dialog.resize(400, 300)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(150, 220, 91,31))
        self.pushButton.setObjectName("PushButton")

        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(100, 50, 200, 150))
        self.label.setObjectName("label")

        self.retranslatedUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslatedUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))

        self.pushButton.setText(_translate("Dialog", "Play Video"))
        self.label.setText(_translate("Dialog", "Video Player"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogWindow = QtWidgets.QMainWindow()
    ui = Ui_Dialog()
    ui.setupUi(DialogWindow)
    DialogWindow.show()
    sys.exit(app.exec_())