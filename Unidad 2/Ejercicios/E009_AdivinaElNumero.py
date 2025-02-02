import random
import sys
from logging import exception

from PyQt5 import uic, QtWidgets
qtCreatorFile = "E009_AdivinaElNumero.ui" # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los signals
        self.btn_adivinar.clicked.connect(self.adivinar)

    # Área de los Slots
    def adivinar(self):
        num = self.txt_num.text()
        numaleatorio = random.randint(1,10)
        if int(num) == numaleatorio:
            self.msj("¡Felicidades! Adivinaste el número.")
            self.close()
        elif int(num) > 10 or int(num) < 1:
            self.msj("Número inválido. Ingresa un número entre 1 y 10")
            self.txt_num.setText("")
        else:
            self.msj("¡Fallaste! El numero era "+str(numaleatorio)+", intenta de nuevo.")
            self.txt_num.setText("")

    def msj (self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())