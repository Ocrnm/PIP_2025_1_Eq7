import sys
from logging import exception

from PyQt5 import uic, QtWidgets
qtCreatorFile = "Proyecto_Unidad1.ui" # Nombre del archivo aquí
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
        self.numeros = []

    # Área de los Slots
    def cargar(self):
        self.txt_lista_numeros.setText("")
        try:
            archivo = open("../Archivos/numeros.csv")
        except:
            self.msj("No se encontró el archivo")
            return
        self.msj("Archivo Cargado con Éxito!")
        contenido = archivo.readlines()
        print(contenido)
        datos = [int(x.strip()) for x in contenido if x.strip().isdigit()]
        print(datos)
        self.numeros.extend(datos)
        self.valor_menor()
        self.valor_mayor()
        self.mediana()
        self.moda()
        self.promedio()
        self.desviacion_estandar()
        self.varianza()
        self.btn_cargar.setEnabled(False)
        self.btn_agregar.setEnabled(True)
        self.btn_guardar.setEnabled(True)
        self.txt_lista_numeros.setText(str(self.numeros))

    def agregar(self):
        calificacion = int(self.txt_numero.text())
        self.numeros.append(calificacion)
        self.valor_menor()
        self.valor_mayor()
        self.mediana()
        self.moda()
        self.promedio()
        self.desviacion_estandar()
        self.varianza()
        self.txt_lista_numeros.setText(str(self.numeros))
        self.btn_cargar.setEnabled(False)

    def valor_menor(self):
        self.txt_minvalue.setText(str(min(self.numeros)))

    def valor_mayor(self):
        self.txt_maxvalue.setText(str(max(self.numeros)))

    def promedio(self):
        prom = sum(self.numeros) / len(self.numeros)
        self.txt_promedio.setText(str(round(prom,2)))

    def mediana(self):
        self.numeros.sort()
        n = len(self.numeros)
        if n % 2 == 0:
            mediana = (self.numeros[n//2] + self.numeros[n//2 - 1]) / 2
        else:
            mediana = self.numeros[n//2]
        self.txt_mediana.setText(str(mediana))

    def moda(self):
        cont = {}
        for c in self.numeros:
            if c in cont:
                cont[c] += 1
            else:
                cont[c] = 1
        moda = max(cont, key=cont.get)
        self.txt_moda.setText(str(moda))

    def desviacion_estandar(self):
        if len(self.numeros) < 2:
            self.txt_desvestandar.setText("0")
            return
        prom = sum(self.numeros) / len(self.numeros)
        desv = (sum((x - prom) ** 2 for x in self.numeros) / (len(self.numeros) - 1)) ** 0.5
        self.txt_desvestandar.setText(str(round(desv, 2)))

    def varianza(self):
        if len(self.numeros) < 2:
            self.txt_varianza.setText("0")
            return
        prom = sum(self.numeros) / len(self.numeros)
        var = sum((x - prom) ** 2 for x in self.numeros) / (len(self.numeros) - 1)
        self.txt_varianza.setText(str(round(var, 2)))

    def guardar(self):
        archivo = open("../Archivos/numeros.csv", "w")
        for c in self.numeros:
            archivo.write(str(c) + "\n")
        archivo.write('Valor Menor: ' + self.txt_minvalue.text() + " \n")
        archivo.write('Valor Mayor: ' + self.txt_maxvalue.text() + " \n")
        archivo.write('Media: ' + self.txt_promedio.text() + " \n")
        archivo.write('Mediana: ' + self.txt_mediana.text() + " \n")
        archivo.write('Moda: ' + self.txt_moda.text() + " \n")
        archivo.write('Desviacion Estandar: ' + self.txt_desvestandar.text() + " \n")
        archivo.write('Varianza: ' + self.txt_varianza.text() + " \n")
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