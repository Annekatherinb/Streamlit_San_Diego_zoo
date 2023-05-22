import models.Animal as animalModel
import models.Habitat as habitatModel
import models.BaseDatos as plataforma
import controllers.ZoologicoController as zooController


class Zoologico:

    def __init__(self, nombre):
        self. nombre = nombre
    def menu(self):


        print("Bienvenido a", self.nombre)
        print("Seleccione la accion que desea realizar: \n")
        base = plataforma.Datos()
        controlador = zooController.ZoologicoController(base, self)
        while True:
            print("1. Ingrese un animal")
            print("2. Mostrar todos los animales")
            print("3. Ingrese las caracteristicas de los habitats")
            print("4. Asignar habitat a un Animal")
            print("5. Mostrar los habitats con los animales")
            print("6. Dieta de los animales")
            print("7. Acciones:\n 1.Jugar\n 2.Dormir\n 3.Comer")
            print("0. Para salir del sistema\n")

            while True:
                try:
                    opcion = int(input("Porfavor ingrese la opcion: "))
                    break

                except ValueError:
                    print("El valor ingresado no es un número entero. Por favor intente nuevamente.")


            if opcion == 0:
                print("- Gracias por visitarnos, vuelva pronto -")
                break

            else:
                controlador.accion(opcion)


    def menu_crearAnimal(self, id):
        juego = 0
        p = True
        while p == True:
            nombre = input("Ingrese el nombre del animal: ")
            if not nombre.isdigit():
                p = False
            else:
                print("Los caracteres que ingresando no son validos, se requiere una cadena de texto\n")

        q = True
        while q == True:
            especie = str(input("Especie del animal: "))
            if not especie.isdigit():
                q = False
            else:
                print("Los caracteres que ingresando no son validos, se requiere una cadena de texto\n")


        while True:
            try:
                habitatTemp = int(input("habitat:\n [1] Selvatico\n [2] Acuatico\n [3] Polar\n [4] Desertico\n [5] Otro\n"))
                if habitatTemp >=1 and habitatTemp <= 5:
                    break
                else:
                    print("Ese valor no existe digitelo nuevamente: ")

            except ValueError:
                print("El valor ingresado no es un número entero. Por favor intente nuevamente.")

        if habitatTemp == 1:
            habitat = "Selvatico"
        elif habitatTemp ==2:
            habitat = "Acuatico"
        elif habitatTemp ==3:
            habitat = "Polar"
        elif habitatTemp ==4:
            habitat = "Desertico"
        elif habitatTemp ==5:
            habitat = input("Digite el nombre del habitat que desea ingresar: ")


        while True:
            try:
                aliTemp = int(input("Alimentacion del animal:\n[1]Herbivoro\n[2]Carnivoro\n[3]Omnivoro\n "))
                if aliTemp >=1 and aliTemp <= 3:
                    break
                else:
                    print("Ese tipo de alimentacion no existe: ")
            except ValueError:
                print("El valor ingresado no es un número entero. Por favor intente nuevamente.")

        if aliTemp == 1:
            alimentacion = "herbivoro"
        elif aliTemp == 2:
            alimentacion = "carnivoro"
        elif aliTemp == 3:
            alimentacion = "omnivoro"

        while True:
            try:
                edad = int(input("Edad del animal: "))
                if edad >=1 and edad <= 200:
                    break
                else:
                    print("Sobrepasa el limite de anios digite nuevamente: ")
            except ValueError:
                print("El valor ingresado no es un número entero. Por favor intente nuevamente.")


        while True:
            try:
                salud = int(input("Salud:\n [1] Saludable\n [2] En revision\n [3] Estado Critico\n "))
                if salud >= 1 and salud <= 3:
                    break  # Salir del bucle si el tipo de datos es correcto
                else:
                    print("Ese valor no existe digitelo nuevamente: ")

            except ValueError:
                print("El valor ingresado no es valido para el tipo de dato que se solicita.")

        while True:
            try:
                horasSueno = int(input("Horas que duerme el animal: "))
                break
            except ValueError:
                print("El valor ingresado no es un número entero. Por favor intente nuevamente.")



        nuevoAnimal = animalModel.Animal(id, nombre,especie, edad, habitat, alimentacion, salud, juego, horasSueno )
        return nuevoAnimal


    def menu_habitat(self, tipo):
        lista_comida = []

        while True:
            try:
                humedadTemp = int(input("Niveles de humedad:\n[1] Alto\n[2] Moderado\n[3] Bajo\n"))
                if humedadTemp >= 1 and humedadTemp <= 3:
                    break  # Salir del bucle si el tipo de datos es correcto
                else:
                    print("Ese valor no existe digitelo nuevamente: ")
            except ValueError:
                print("El valor ingresado no es un número entero. Por favor intente nuevamente.")

        if humedadTemp == 1:
            humedad = "Alta"
        elif humedadTemp == 2:
            humedad = "Moderada"
        elif humedadTemp == 3:
            humedad = "Baja"

        p = True
        while p == True:
            clima = input("Que clima tiene: ")
            if not clima.isdigit():
                p = False
            else:
                print("Los caracteres que ingresando no son validos, se requiere una cadena de texto\n")

        while True:
            try:
                temperatura = int(input("Digite el valor de la temperatura: "))
                break  # Salir del bucle si el tipo de datos es correcto

            except ValueError:
                print("El valor ingresado no es un número entero. Por favor intente nuevamente.")

        while True:
            try:
                capacidad = int(input("Cual es la capacidad maxima de este habitat: "))
                break  # Salir del bucle si el tipo de datos es correcto

            except ValueError:
                print("El valor ingresado no es un número entero. Por favor intente nuevamente.")

        while True:
            alimento = input("Ingrese un tipo de dieta o escriba 'fin' para finalizar: ")
            if alimento == 'fin':
                break
            if alimento.isdigit():
                print("Entrada no válida. Debe ingresar un texto.")
            else:
                lista_comida.append(alimento)

        nuevoHabitat = habitatModel.Habitat(tipo, humedad, clima, temperatura, capacidad, lista_comida)
        return nuevoHabitat

    def solicitar_animal(self, mensaje):
        return input(mensaje)

