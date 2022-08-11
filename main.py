import os
import linecache

class Estudiante:
    def __init__(self, nombre, numero_estudiante):
        self._nombre = nombre
        self._numero_estudiante = numero_estudiante

    # nombre getter method
    def get_nombre(self):
        return self._nombre

    # nombre setter method
    def set_nombre(self, x):
        self._nombre = x

    # numero_estudiante getter method
    def get_numero_estudiante(self):
        return self._numero_estudiante

    # numero_estudiante setter method
    def set_numero_estudiante(self, x):
        self._numero_estudiante = x

class Evaluacion:
    def __init__(eva, evaluacion, puntos, porciento):
        eva._evaluacion = evaluacion
        eva._puntos = puntos
        eva._porciento = porciento

    # evaluacion getter method
    def get_evaluacion(eva):
        return eva._evaluacion

    # evaluacion setter method
    def set_evaluacion(eva, x):
        eva._evaluacion = x

    # puntos getter method
    def get_puntos(eva):
        return eva._puntos

    # puntos setter method
    def set_puntos(eva, x):
        eva._puntos = x

    # porciento getter method
    def get_porciento(eva):
        return eva._porciento

    # porciento setter method
    def set_porciento(eva, x):
        eva._porciento = x

class Curso(Estudiante, Evaluacion):
    def __init__(cur, curso, archivoName, qtyEval):
        cur._curso = curso
        cur._archivoName = archivoName
        cur._qtyEval = qtyEval

    # curso getter method
    def get_curso(cur):
        return cur._curso

    # curso setter method
    def set_curso(cur, x):
        cur._curso = x

    # archivoName getter method
    def get_archivoName(cur):
        return cur._archivoName

    # archivoName setter method
    def set_archivoName(cur, x):
        cur._archivoName = x

    # qtyEval getter method
    def get_qtyEval(cur):
        return cur._qtyEval

    # qtyEval setter method
    def set_qtyEval(cur, x):
        cur._qtyEval = x

def crearArchivoEstudiantes():
    i = 0
    print("Ingrese el nombre del archivo donde se almacenará los estudiantes, Ejemplo: estudiantes202230.txt")
    nombreArchivo = input()
    if os.path.exists(str(nombreArchivo)): #verifica si el archivo existe
        print("El nombre del achivo ya existe, favor intentar con otro nombre")
        crearArchivoEstudiantes() #regresa al inicio de la funcion
    else: #si el archivo no existe
        file1 = open(nombreArchivo, "a") #crea el archivo
        print("¿Cúantos estudiantes desea añadir?")
        n = int(input())
        file1.write(str(n) + "\n") #escribe en el archivo la cantidad de estudiantes
        while i < n: #mientras i sea menor que la cantidad de estudiantes
            print("Nombre de Estudiante " + str(i + 1) + " en el formato Apellido(s), Nombre: ")
            nombreEstudiante = input()
            print("Número de Estudiante de " + nombreEstudiante + " : ")
            numeroEstudiante = input()
            file1.write(nombreEstudiante + "\n") #escribe el nombre del estudiante en el archivo
            file1.write(numeroEstudiante + "\n") #escribe el numero de estudiante en el archivo
            i = i + 1 #incremente el valor de i las n veces que corra el while
        file1.close() #cierra el archivo

def crearRegistro():
    i = 0
    n = 0
    choice = 0
    print("Ingrese el nombre del archivo de configuración para el registro de notas "
          "(para un curso particular). Ejemplo: NavaCOMP3800.txt")
    archivoConfig = input()

    if os.path.exists(str(archivoConfig)): # verifica si el nombre del archivo de configuracion existe,
        # si existe vuelve al inicio de la funcion
        print("El nombre del achivo ya existe, favor intentar con otro nombre")
        crearRegistro()
    else: # si no existe entonces le permite ir creando el archivo
        print("Ingrese el nombre del curso. Ejemplo: COMP 3800 Lenguajes de Programación")
        nombreCurso = input()
        print("Ingrese el nombre del archivo con nombres y ID de estudiantes. Ejemplo: comp3800estuds.txt")
        archivoName = input()
        if os.path.exists(str(archivoName)): # verifica si el nombre del archivo que contiene la informacion del los estudiantes existe
            # si existe permite continuar con el programa
            print("Ingrese cuantas evaluaciones tendrá el curso")
            n = int(input())
            file1 = open(archivoConfig, "a") #abre el archivo
            file1.write(nombreCurso + "\n") #escribe el nombre del curso
            file1.write(str(archivoName) + "\n") #escribe el nombre del archivo que contiene los nombres de estudiantes
            file1.write(str(n) + "\n")  #escribe cuantas evaluaciones tendra el curso
        else:  #Si no existe, le da la opción al usuario de volverlo a intentar o regresar a main
            print("-------No existe el archivo-------")
            print("Presione: 1- Volver a intentar")
            print("Presione: Cualquier tecla para salir")
            print("----------------------------------")
            print("Ingrese una Opción: ")
            choice = input()
            if choice == "1": #si no existe el archivo y el usuario presiona el 1
                crearRegistro() #se vuelve a ejecutar la funcion crear registro
            else: #si presiona otra tecla
                return #regresa a main
        while i < n: #mientras i sea menor que las evaluaciones que tendra el curso
            print("Nombre Evaluación " + str(i + 1) + ": ")
            nombreEvaluacion = input()
            print("Total puntos " + nombreEvaluacion + ": ")
            puntos = float(input())
            print("Por ciento de contribución " + nombreEvaluacion + " para promedio final: ")
            promedio = float(input())
            file1.write(nombreEvaluacion + "\n") #escribe el nombre de la evaluacion en el archivo
            file1.write(str(puntos) + "\n") #escribe los puntos de la evaluacion en el archivo
            file1.write(str(promedio) + "\n") #escribe el promedio de la evaluacion en el archivo
            i = i + 1
        file1.close()  # cierra el archivo
def cargarDatosNoEst(l):
    lista = l
    lista.clear()
    read = open(archivoConfig) #abre el archivo de configuracion
    nombreCurso = read.readline() #lee la primera linea y la almacena en la variable
    archivoEst = read.readline() #lee la segunda linea y la almacena en la variable
    cantidad = read.readline()#lee la tercera linea y la almacena en la variable
    lista.append(Curso(nombreCurso,archivoEst,cantidad)) #guarda en el arreglo lista[0] el contenido de las variables

    i = 0
    while i < int(cantidad): #mientras i sea menor que la cantidad de evaluaciones
        evaluacion = read.readline() #lee la cuarta linea y la almacena en la variable
        puntos = read.readline() #lee la quinta linea y la almacena en la variable
        porciento = read.readline() #lee la sexta linea y la almacena en la variable
        lista.append(Evaluacion(evaluacion, puntos, porciento)) #guarda en el arreglo lista[] el contenido de las variables (cantidad) veces.
        i += 1 #incrementa el valor de 1 hasta que alcance a leer todas las evaluaciones
    read.close() #cerramos el archivo de configuracion
    read = open(archivoEst.strip()) #abrimos el archivo que contiene la informacion de los estudiantes
    qty = read.readline()  #lee la primera linea que contiene la cantidad de los estudiantes y la almacena en la variable
    j = 0
    while j < int(qty): #mientras j sea menor que la cantidad de estudiantes
        nombre = read.readline() #lee la segunda, cuarta, sexta, octava, (qty veces de 2 en 2) linea y la almacena en la variable
        numEst = read.readline() #lee la tercera, quinta, septima, novena, (qty veces de 2 en 2) linea y la almacena en la variable
        lista.append(Estudiante(nombre, numEst)) #guarda en el arreglo lista[] el contenido de las variables (qty) veces.
        k = 0
        while k <= int(cantidad): #mientra k sea menor que la cantidad de evaluaciones
            lista.append(0) #se ingresan ceros a los valores delarreglo
            k += 1 #se incrementa k h
        j += 1

def cargarDatosSiEst(l):  # este metodo trae la lista como argumento
    lista = l
    lista.clear()  # se borra el contenido de la lista
    read = open(archivoConfig)  # se abre el archivo de configuracion
    # las siguientes 3 lineas son guardadas en variables
    nombreCurso = read.readline()
    archivoEst = read.readline()
    cantidad = read.readline()
    lista.append(Curso(nombreCurso, archivoEst,
                       cantidad))  # se añade a la lista un objeto tipo Curso usando las 3 variables como argumentos

    i = 0
    while i < int(cantidad):  # loop que se repite por la cantidad de evaluaciones
        # las siguientes 3 lineas son guardadas en variables
        evaluacion = read.readline()
        puntos = read.readline()
        porciento = read.readline()
        lista.append(Evaluacion(evaluacion, puntos,
                                porciento))  # se añade a la lista un objeto tipo Evaluacion usando las 3 variables como argumentos
        i += 1
    read.close()  # se cierra el archivo al terminar el loop
    read = open(archivoEst.strip())  # se abre el archivo de estudiantes
    # las siguientes 2 lineas son guardadas en variables
    qty = read.readline()
    qnty = int(cantidad)

    # Se utiliza la variable lineNumber para determinar en que linea se encuentra el primer nombre en el archivo de configuracion
    lineNumber = (qnty * 3) + 3  # se utiliza esta formula porque "qnty" es la cantidad de examenes,
    # *3 porque hay tres lineas por cada examen (nombre, puntos, peso)
    # +3 porque siempre van a haber 3 lineas al principio del archivo (nombreCurso, archivoEst, Cantidad)

    file = open(archivoConfig)  # se abre el archivo de configuracion
    content = file.readlines()  # se almacenan las lineas leidas en "content"
    nombre = content[lineNumber]  # se guarda el primer nombre del archivo en la variable "nombre"

    lines = []  # utilizaremos esta lista para guardar la informacion de los estudiantes(nombre,ID, notas, promedio)
    fullCounter = 0
    with open(archivoConfig) as fp:  # se abre el archivo de configuracion
        for line in fp:
            if line.strip():
                fullCounter += 1  # se cuentan cuantas lineas hay en total en el archivo

    for x in range(lineNumber + 1,
                   fullCounter + 1):  # loop que se repite desde la linea del nombre hasta el final del archivo
        line = linecache.getline(archivoConfig, x)  # se obtiene el valor de cada linea
        lines.append(line.strip())  # se almacenan los valores en la lista "lines"

    j = 0
    cnt = 0
    x = 0
    while j < int(
            qty):  # nested loop para append los valores leidos del archivo y guradarlos en la lista que se utiliza en el programa
        lista.append(Estudiante(lines[x], lines[
            x + 1]))  # se agrega un objeto tipo estudiante con las posicione x, x+1 (nombre, id) como argumento
        k = 0
        while k <= int(cantidad):  # loop que se repite por la cantidad de examenes
            lista.append(
                lines[cnt + 2])  # se agrega a la lista la posicion [cnt+2] (a partir de la primera nota + contador)
            k += 1
            cnt += 1
        cnt += 2  # se le suma 2 porque las proximas dos posiciones son nombre y ID, y solo queremos las notas
        j += 1
        x += qnty + 3  # se le suma qnty + 3 para que la variable x termine en el proximo nombre en la lista


def entrarParaTodos():
    i = 0

    print("---Configuración del curso--")
    print("Nombre del curso: " + lista[i].get_curso().strip()) #lee de lista[0].get_curso()
    print("Nombre del archivo con nombres y ID de estudiantes: " + lista[i].get_archivoName().strip()) #lee de lista[0].get_archivoName()
    print("Evaluaciones que tendá el curso: " + str(lista[i].get_qtyEval().strip())) #lee de lista[0].get_qtyEval()
    cantidad = int(lista[i].get_qtyEval()) #almacenamos la cantidad de evaluaciones que tendra el curso
    i += 1 #se incrementa el index
    while i <= cantidad: #mientras i sea menor o igual que la cantidad de evaluaciones
        print("Valor del Index [" + str(i) +"]: " + lista[i].get_evaluacion().strip()) #lee de lista[i].get_qtyEval() por (cantidad veces)
        i += 1
    print("¿Para cual actividad desea añadir los puntos? (Valor del Index [])")
    valorEvaluacion = input() #recibimos del usuario que actividad es la que queremos entrar los puntos
    x = int(valorEvaluacion)
    while i < int(len(lista)): #mientras i sea menor que el largo de la lista
        print("---------Estudiante---------")
        print("Nombre: " + lista[i].get_nombre().strip())
        print("Número de Estudiante: " + lista[i].get_numero_estudiante().strip())
        print("El valor de examen de la actividad " + lista[x].get_evaluacion().strip() + ": " + lista[x].get_puntos().strip())
        print("Ingrese la nota del examen")
        lista[i + x] = input() #añadimos la nota del examen a la lista
        j = 0
        while j <= cantidad+1:
            i += 1
            j += 1

def entrarParaUno():
    i = 0

    print("---Configuración del curso--")
    print("Nombre del curso: " + lista[i].get_curso().strip())
    print("Nombre del archivo con nombres y ID de estudiantes: " + lista[i].get_archivoName().strip())
    print("Evaluaciones que tendá el curso: " + str(lista[i].get_qtyEval().strip()))
    cantidad = int(lista[i].get_qtyEval())
    i += 1

    while i <= cantidad:
        print("Valor del Index [" + str(i) +"]: " + lista[i].get_evaluacion().strip())
        i += 1
    print("¿Para cual actividad desea añadir los puntos? (Valor del Index [])" )
    valorEvaluacion = input()
    x = int(valorEvaluacion)
    while i < int(len(lista)):
        print("---------Estudiante---------")
        print("Valor del Index [" + str(i) +"]: " + lista[i].get_nombre().strip())
        print("Número de Estudiante:" + lista[i].get_numero_estudiante().strip())
        i += 1
        j = 0
        while j < int(cantidad):
            j += 1
            i += 1
        i += 1
    print("¿Para cual estudiante desea añadir los puntos? (Valor del Index [])")
    valorEstudiante = input()
    y = int(valorEstudiante)
    print("---------Estudiante---------")
    print("Nombre:" + lista[y].get_nombre().strip())
    print("Número de Estudiante:" + lista[y].get_numero_estudiante().strip())
    y += x
    print("El valor de examen es: " + lista[x].get_puntos().strip())
    print("Ingrese la nota del examen")
    lista[y] = input()

def contieneNombres():
    global foundName
    read = open(archivoConfig)
    nombreCurso = read.readline()
    archivoEst = read.readline()
    read.close()

    read = open(archivoEst.strip())
    qty = read.readline()
    nombre = read.readline()
    with  open(archivoConfig, 'r') as input:
        for line in input:
            if nombre in line:
                foundName = True
                break

def guardarDatos():
    #se declaran las variables y arreglos que se utilizaran en la funcion
    i = 0
    promedio = []
    porciento = []
    puntos = []
    l = 0
    cantidad = int(lista[i].get_qtyEval())
    i += 1
    found = False
    while i <= cantidad: #loop se repite la cantidad de veces que hayan evaluaciones
        evaluacion = lista[i].get_evaluacion().strip() #se obtiene el nombre de la evaluacion y se guarda en la variable "evaluacion
        porcientos = float(lista[i].get_porciento().strip()) / float(100)  #se calcula el peso del examen dividiendo el valor entre 100 y se guarda en la variable "porcientos"
        porciento.append(porcientos)  # Luego de calcularse, se agrega a la lista "porciento"
        puntos.append(evaluacion)  # se agrega a la lista "puntos" la variable "evaluacion"
        i += 1

    nombre = lista[i].get_nombre().strip() #se guarda el nombre del primer estudiante en la lista en la variable "nombre"
    Counter = 0
    with  open(archivoConfig, 'r') as input: #se abre el archivo de configuracion para leerlo
        for line in input: #este loop se repite la cantidad de veces que se lea una linea del archivo
            Counter += 1 #se incrementa el contador por cada linea leída
            if nombre in line:
                found = True
                break #si el nombre del estudiante se encuentra en la linea se para de leer el archivo

    if found == False: #si no hay nombre en el archivo de configuracion se ejecuta este bloque
        file = open(archivoConfig, "a") #se abre el archivo de configuracion en modo de apendizar

        while i < int(len(lista)): #nested loop que se repite hasta el final de la lista
            #se escribe en la lista el archivo el nombre y el ID del estudiante
            file.write(lista[i].get_nombre().strip() + "\n")
            file.write(lista[i].get_numero_estudiante().strip() + "\n")
            i += 1
            j = 0
            while j < int(cantidad): #loop que se repite por la cantidad de evaluaciones
                puntosObtenidos = float(lista[i]) #se obtienen los puntos obtenidos de la posicion i en la lista
                file.write(str(puntosObtenidos) + "\n") #se escribe en el archivo los puntos obtenidos
                valorExam = float(lista[j + 1].get_puntos()) #se obtiene el valor del examen en la posicion j+1 de la lista
                prom = puntosObtenidos / valorExam * 100 * porciento[j] #se calcula el promedio
                promedio.append(prom) #se agrega el promedio al arreglo "promedio"
                j += 1
                i += 1
            k = 0
            promedioTotal = 0
            while k < int(cantidad): #Loop que se repite por la cantidad de evaluaciones
                promedioTotal = promedioTotal + promedio[l] #se calcula el promedio total
                l += 1
                k += 1
            file.write(str(promedioTotal) + "\n") #se escribe el promedio total en el archivo
            i += 1
        file.close()

    if found == True: #si ya hay nombre en el archivo de configuracion se ejecuta este bloque
        lines = [] #se crea un arreglo "lines"
        with open(archivoConfig) as f:
            for line in iter(lambda: f.readline().rstrip(), nombre): #se lee el archivo hasta que llegue al nombre
                lines.append(line) #se guardan las lineas leidas en la lista "lines"
        f.close()
        file = open(archivoConfig, "w") #se abre el archivo de configuracion en modo "write"
        for eachLine in lines:
            file.write(eachLine+"\n") #se escribe el la lista "lines" en el archivo
                                      #lo cual contiene las primeras lineas del archivo
        file.close() #se cierra el archivo

        file = open(archivoConfig, "a") #se vuelve a abrir el archivo en modo de apendizar
                                        #y basicamente se ejecuta el mismo bloque de instrucciones para cuando found == False
        while i < int(len(lista)):
            file.write(lista[i].get_nombre().strip() + "\n")
            file.write(lista[i].get_numero_estudiante().strip() + "\n")
            i += 1
            j = 0
            while j < int(cantidad):
                puntosObtenidos = float(lista[i])
                file.write(str(puntosObtenidos) + "\n")
                valorExam = float(lista[j + 1].get_puntos())
                prom = puntosObtenidos / valorExam * 100 * porciento[j]
                promedio.append(prom)
                j += 1
                i += 1
            k = 0
            promedioTotal = 0
            while k < int(cantidad):
                promedioTotal = promedioTotal + promedio[l]
                l += 1
                k += 1
            file.write(str("{:.2f}".format(promedioTotal)) + "\n")
            i += 1
        file.close()
    print("Datos guardados exitosamente")

def verTodo():
    #Se declaran las variables y arreglos que se utilizaran en la funcion
    i = 0
    promedio = []
    porciento = []
    puntos = []
    l = 0
    #imprime la configuracion del curso la cual se encuentra en el objeto de la primera posicion de la lista
    print("---Configuración del curso--")
    print("Nombre del curso: " + lista[i].get_curso().strip())
    print("Nombre del archivo con nombres y ID de estudiantes: c" + lista[i].get_archivoName().strip())
    print("Evaluaciones que tendá el curso: " + str(lista[i].get_qtyEval().strip()))
    cantidad = int(lista[i].get_qtyEval())
    i += 1 #Se incrementa i para continuar a la segunda posicion de la lista

    #Se hace un loop que se repite la cantidad de veces que hayan
    while i <= cantidad: #El signo de <= se utiliza en este caso porque i comienza en 1 en vez de 0
        print("Nombre Evaluación: " + lista[i].get_evaluacion().strip())
        evaluacion = lista[i].get_evaluacion().strip() #se obtiene el nombre de la evaluacion y se guarda en la variable "evaluacion
        print("Total puntos para "+ evaluacion + " : " + str(lista[i].get_puntos().strip()))
        print("Por ciento de contribución de "+ evaluacion +" para promedio final: " + str(lista[i].get_porciento().strip()))
        porcientos = float(lista[i].get_porciento().strip())/float(100) #se calcula el peso del examen dividiendo el valor entre 100 y se guarda en la variable "porcientos"
        porciento.append(porcientos) #Luego de calcularse, se agrega a la lista "porciento"
        puntos.append(evaluacion) #se agrega a la lista "puntos" la variable "evaluacion"
        i += 1

    #se hace un nested loop que se repite desde el valor de i hasta el final de la lista
    while i < int(len(lista)):
        #el primer loop imprime los nombres de los estudiantes y sus IDs
        print("---------Estudiante---------")
        print("Nombre:" + lista[i].get_nombre().strip())
        print("Número de Estudiante:" + lista[i].get_numero_estudiante().strip())
        i += 1
        j = 0
        # el segundo loop imprime las notas obtenidas
        while j < int(cantidad): #en este caso no se utiliza "<=" porque j = 0
            puntosObtenidos = float(lista[i]) #Se obtiene los puntos obtenidos de la posicion i en la lista
            print(str(puntos[j]) + ": " + str(puntosObtenidos))
            valorExam = float(lista[j + 1].get_puntos()) #se obtiene el valor del examen de la posicion j+1 de la lista
            prom = puntosObtenidos/valorExam*100*porciento[j] #se calcula el promedio
            promedio.append(prom) #se agrega el promedio a la lista "promedio"
            j += 1
            i += 1
        k = 0
        promedioTotal = 0
        while k <int(cantidad): #en este loop se calcula el promedio total y lo imprime
            promedioTotal = promedioTotal + promedio[l]
            l += 1
            k += 1
        print("Promedio Final del Curso: " + str("{:.2f}".format(promedioTotal)))
        i += 1

# Main
menuChoice = 0
lista = []
foundName = False
while menuChoice != 8:
    print("1- Crear archivo con nombres y número de estudiantes")
    print("2- Crear configuración del curso")
    print("3- Cargar configuración del curso al programa")
    print("4- Ver todos los nombres con sus ID, todas las puntuaciones y el promedio final del curso")
    print("5- Entrar las puntuaciones para una actividad particular para todos los estudiantes")
    print("6- Entrar la puntuación para una actividad particular para un estudiante particular")
    print("7- Guardar los datos")
    print("8- Salir del programa")
    print("Seleccione una Opción")
    menuChoice = int(input())
    if menuChoice == 1:
        crearArchivoEstudiantes()
    else:
        if menuChoice == 2:
            crearRegistro()
        else:
            if menuChoice == 3:
                print("Ingrese el nombre del archivo de configuración:")
                archivoConfig = input()
                if os.path.exists(str(archivoConfig)):
                    contieneNombres()
                    if foundName == False:
                        cargarDatosNoEst(lista)
                        print("No se encuentran datos de estudiantes en el archivo")
                    if foundName == True:
                        cargarDatosSiEst(lista)
                        print("El archivo fue cargado al programa exitosamente")
                else:
                    print("El archivo no existe, vuelva a intentarlo")
            else:
                if menuChoice == 4:
                    if lista:
                        verTodo()
                        print("----------------------------")
                    else:
                        print("Cargue primero el archivo de configuración al curso")
                else:
                    if menuChoice == 5:
                        entrarParaTodos()
                    else:
                        if menuChoice == 6:
                            entrarParaUno()
                        else:
                            if menuChoice == 7:
                                guardarDatos()
                            else:
                                if menuChoice != 8:
                                    print(lista)
                                    print('Opción incorrecta, vuelva a intentarlo')