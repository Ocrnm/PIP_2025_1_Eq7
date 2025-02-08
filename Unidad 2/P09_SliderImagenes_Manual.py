import sys
from PyQt5 import uic, QtWidgets, QtGui
qtCreatorFile = "P09_SliderImagenes_Manual.ui" # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los signals
        self.selectorImagen.setMinimum(1)
        self.selectorImagen.setMaximum(3)
        self.selectorImagen.setSingleStep(1)
        self.selectorImagen.setValue(1)
        self.selectorImagen.valueChanged.connect(self.cambiaValor)

        self.diccionarioDatos = {
            1: (":/Ejercicios/8s85l9yb14k81.png",["Jesse Pinkman","20","Chef"]),
            2: (":/Ejercicios/3ueemqhb14k81.png",["Walter White","50","Químico"]),
            3: (":/Ejercicios/john cena.png", ["John Cena","47","Actor"]),
        }
        self.indice = 1
        self.obtenerDatos()

    # Área de los Slots
    def obtenerDatos(self):
        nombre = self.diccionarioDatos[self.indice][1][0]
        edad = self.diccionarioDatos[self.indice][1][1]
        ocupacion = self.diccionarioDatos[self.indice][1][2]
        self.txt_nombre.setText(nombre)
        self.txt_edad.setText(edad)
        self.txt_ocupacion.setText(ocupacion)

        self.imagen_descripcion.setPixmap(QtGui.QPixmap(self.diccionarioDatos[self.indice][0]))


    def cambiaValor(self):
        self.indice = self.selectorImagen.value()
        self.obtenerDatos()
       # self.txt_valor.setText(str(value))

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())