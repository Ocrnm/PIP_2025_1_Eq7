import sys
from logging import exception

from PyQt5 import uic, QtWidgets
qtCreatorFile = "P08_PromedioNumeros-Load_V2.ui" # Nombre del archivo aquí
Ui_MainWindow, QtBaseClass = uic.loadUiType(qtCreatorFile)
class MyApp(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        # Área de los signals
        self.btn_cargar.clicked.connect(self.cargar)
        self.btn_agregar.clicked.connect(self.agregar)
        self.btn_guardar.clicked.connect(self.guardar)
        self.calificaciones = []

    # Área de los Slots
    def cargar(self):
        self.txt_lista_calificaciones.setText("")
        ## TAREA EJ 10 ---, COMO COMPRUEBO SI EL ARCHIVO EXISTE ?
        try:
            archivo = open("../Archivos/calificaciones.csv")
        except:
            self.msj("No se encontró el archivo")
            return
        self.msj("Archivo Cargado con Éxito!")
        contenido = archivo.readlines()
        print(contenido)
        datos = [int(x) for x in contenido]
        print(datos)
        # TAREA EJ 11 ---, EN VEZ DE SOBREESCRIBIR, CONCATENAR
        self.calificaciones.extend(datos)
        self.promedio()
        # TAREA EJ 12. --- ASEGURARSE DE QUE SOLO SE PUEDA CARGAR ANTES DE AGREGAR LA PRIMERA CALIFICACION (ENABLE)
        self.btn_cargar.setEnabled(False)
        self.btn_agregar.setEnabled(True)
        self.btn_guardar.setEnabled(True)
        self.txt_lista_calificaciones.setText(str(self.calificaciones))

    def agregar(self):
        calificacion = int(self.txt_calificacion.text())
        self.calificaciones.append(calificacion)
        self.promedio()
        self.txt_lista_calificaciones.setText(str(self.calificaciones))
        self.btn_cargar.setEnabled(False) # TAREA EJ 12

    def promedio(self):
        prom = sum(self.calificaciones) / len(self.calificaciones)
        self.txt_promedio.setText(str(prom))

    def guardar(self):
        archivo = open("../Archivos/calificaciones.csv", "w") # w ---- write ----- a ---- apppend
        for c in self.calificaciones:
            archivo.write(str(c) + " \n")
        archivo.flush()
        archivo.close()
        self.msj("Archivo Guardado con Éxito!")
        self.btn_cargar.setEnabled(True)

    def msj (self,txt):
        m = QtWidgets.QMessageBox()
        m.setText(txt)
        m.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())