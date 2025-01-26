import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E001_IMC.ui" # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los signals
        self.btn_calcIMC.clicked.connect(self.imc)

    # Área de los Slots
    def imc(self):
            peso = float(self.txt_peso.text())
            estatura = float(self.txt_estatura.text())
            imc = f'{peso/(estatura**2):.2f}'
            self.msj("Su Índice de Masa Corporal es: "+str(imc))

    def msj (self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())