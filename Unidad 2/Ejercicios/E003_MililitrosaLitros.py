import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E003_MililitrosaLitros.ui" # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los signals
        self.txt_L.setEnabled(False)
        self.txt_ml.textChanged.connect(self.ml_a_l)

    # Área de los Slots
    def ml_a_l(self):
        try:
            value = self.txt_ml.text()
            L = float(value) / 1000
            self.txt_L.setText(str(L))
        except:
            self.txt_L.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())