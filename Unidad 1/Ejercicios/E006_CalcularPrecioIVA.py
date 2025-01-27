import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E006_CalcularPrecioIVA.ui" # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los signals
        self.btn_calcIVA.clicked.connect(self.calcular_IVA)

    # Área de los Slots
    def calcular_IVA(self):
        precio = float(self.txt_cantidad.text())
        iva = precio*0.16
        precio_iva = precio+iva
        self.msj("El IVA es: $"+str(iva)+" siendo el precio con IVA: $"+str(precio_iva))

    def msj (self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())