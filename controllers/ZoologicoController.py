
import streamlit as st
class ZoologicoController:


    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista


    def accion(self, opcion):

        if opcion == 1:
            st.subheader("ID del Animal:")
            id = st.number_input("Ingresar ID :", min_value=0, key="id")
            verificacion = self.modelo.verificar_animal(id)
            if verificacion == 0:
                animal = self.vista.menu_crearAnimal(id)
                if animal is not None:
                    self.modelo.ingresar_animal(animal.id, animal)
                    self.modelo.ingresar_habitat(animal.habitat)
            else:
                st.info("Ya existe un animal con ese id.")

        if opcion == 2:
            #self.modelo.leer_animal()
            self.modelo.catalogo_animales()

        if opcion == 3:
            st.subheader("Tipo")
            #st.write(self.modelo.leer_habitat())
            tipo = st.text_input("De los que se muestran en pantalla de acuerdo a los animales agregados", key= "tipo")
            comprobador = self.modelo.verificar(tipo)
            if comprobador == 0:
                habitat = self.vista.menu_habitat(tipo)
                if habitat is not None:
                    self.modelo.caracteristicas_habitat(tipo, habitat)
            else:
                st.info("No existe aun.")

        """

if opcion == 2:
self.modelo.leer_animal()

if opcion == 3:
self.modelo.leer_habitat()
tipo = input("Digite el habitat al que le quiere asignar las caractericas: ")
verificacion = self.modelo.verificar(tipo)
if verificacion == 1:
    habitat = self.vista.menu_habitat(tipo)
    self.modelo.caracteristicas_habitat(tipo, habitat)
else:
    print("Ese habitat no existe dentro los habitats asignados de oringen de los animales actualmente agregados\n")

if opcion == 4:

print("Ingrese uno de las habitat que se ven en pantalla:\n")
self.modelo.mostrar_habitat()
print("")
while True:
    try:
        pTempA = int(input("Digite el id del animal que quiere ubicar en un habitat: "))
        break  # Salir del bucle si el tipo de datos es correcto
    except ValueError:
        print("El valor ingresado no es un número entero. Por favor intente nuevamente.")

pTempH = input("Ingrese el habitat donde lo quiere ubicar: ")
pClima = input("Ingrese el clima adecuado: ")
self.modelo.animal_habitat(pTempA, pTempH, pClima)

if opcion == 5:
self.modelo.mostrar_asignados()

if opcion == 6:
print("[1]Carnivoro.\n [2]Herbivoro.\n [3]Omnivoro.")
while True:
    dieta=input("Ingrese el tipo de dieta")
    if dieta.isdigit():
        break
    else:
        print("Entrada no valida")

while True:
    alimentos = input("Ingrese un alimento a agregar o escriba 'fin' para finalizar: ")
    if alimentos == 'fin':
        break
    if alimentos.isdigit():
        print("Por favor ingrese texto.")
    else:
        self.modelo.agregar_alimentos()
"""



