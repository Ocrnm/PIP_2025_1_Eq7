import sys
from PyQt5 import uic, QtWidgets
qtCreatorFile = "P08_DescripcionDeImagenes.ui" # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los signals
        self.selectorImagen.setMinimum(1)
        self.selectorImagen.setMaximum(1)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(1)
        self.selectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarioDatos = {
            0: (":/Ejercicios/8s85l9yb14k81.png",["Jesse Pinkman","20","Chef"]),
            1: (":/Ejercicios/3ueemqhb14k81.png",["Walter White","50","Químico"]),
        }
        self.indice = 0
        self.obtenerDatos(self.indice)

    # Área de los Slots
    def obtenerDatos(self, clave):
        nombre = self.diccionarioDatos[clave][1][0]
        edad = self.diccionarioDatos[clave][1][1]
        ocupacion = self.diccionarioDatos[clave][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_edad.setText(edad)
        self.txt_ocupacion.setText(ocupacion)


    def cambiaValor(self):
        value = self.selectorImagen.value()
        self.txt_valor.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())