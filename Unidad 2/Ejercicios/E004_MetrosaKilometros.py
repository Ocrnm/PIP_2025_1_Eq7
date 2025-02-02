import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "E004_MetrosaKilometros.ui" # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los signals
        self.txt_km.setEnabled(False)
        self.txt_m.textChanged.connect(self.m_a_km)

    # Área de los Slots
    def m_a_km(self):
        try:
            value = self.txt_m.text()
            km = float(value) / 1000
            self.txt_km.setText(str(km))
        except:
            self.txt_km.setText("")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())