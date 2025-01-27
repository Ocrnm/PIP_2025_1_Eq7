import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E005_AreaRectangulo.ui" # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los signals
        self.btn_calcArea.clicked.connect(self.calcular_area_rectangulo)

    # Área de los Slots
    def calcular_area_rectangulo(self):
        base = float(self.txt_base.text())
        altura = float(self.txt_altura.text())
        area = base*altura
        self.msj("El área del rectángulo es: "+str(area)+" m² (metros cuadrados)")

    def msj (self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())