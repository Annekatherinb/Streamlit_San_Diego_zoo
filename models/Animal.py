

class Animal:

    def __init__(self, id, nombre, especie, edad, habitat, alimentacion, salud, juego, horasSueno ):
        self.id = id
        self.nombre = nombre
        self.especie = especie
        self.edad = edad
        self.habitat = habitat
        self.alimentacion = alimentacion
        self.salud = salud
        self.juego = juego
        self. horasSueno = horasSueno

    def mostrarAnimal(self):
        print( "Asignado con el numero:", self.id, "de nombre: ", self.nombre, "es una/un: ",self.especie, self.habitat, "\n")


