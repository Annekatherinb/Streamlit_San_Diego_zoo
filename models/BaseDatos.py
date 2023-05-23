import models.Animal as animalModel
import streamlit as st
class Datos:
    def __init__(self):

        self.animales = {}

        if "habitat" in st.session_state:
            self.habitats = st.session_state["habitat"]
        else:
            self.habitats = []

        self.habitat_fijo = {}
        self.asignacion = {}
        self.alimentacion = {}

    def ingresar_animal(self,id, animal):
        self.animales[id] = animal


    def verificar_animal(self, id):
        if self.animales.get(id) is not None:
            return 1
        else:
            return 0

    def leer_animal(self):
        print("Animales ingresados al zoologico:\n")
        st.write(self.animales)
        for key in self.animales:
            animal = self.animales[key]
            st.write(f'El animal de id{key}, se llama{animal.nombre}, y es un/a {animal.especie}')


    def ingresar_habitat(self, habitat):
        if habitat in self.habitats:
            st.warning("Ya se encuentra agregado ese Habitat al zoologico\n")
        else:
            self.habitats.append(habitat)

    def leer_habitat(self):
        print("Los habitats ingresados hasta el momento son: ")
        st.write(self.habitats)


    def caracteristicas_habitat(self, habitat, ob_Habi):
        if habitat not in self.habitat_fijo:
            self.habitat_fijo[habitat] = []

        self.habitat_fijo[habitat].append(ob_Habi)
        print("El habitat fue creado existosamente, dentro del zoologico\n")

    def mostrar_habitat(self):
        for tipo, habitats in self.habitat_fijo.items():
            print(f"Hábitats de tipo {tipo}:")
            for habitat in habitats:
                print(f"Clima:{habitat.clima} y Temperatura de: {habitat.temperatura} con una Humedad: {habitat.humedad} de capacidad: {habitat.capacidad} y solo permite animales de alimentacion: {habitat.alimentacion}")


    def verificar(self, tipo):
        for i in range(len(self.habitats)):
            if tipo in self.habitats:
                return 1
            else:
                return 0
                st.warning("Desconocido")

    def animal_habitat(self, id, habitat,clima):
        if id in self.animales:
            animal = self.animales[id]
            if habitat in self.habitat_fijo:
                lista = self.habitat_fijo[habitat]
                if any(h.tipo == habitat for h in lista):
                    if any(h.clima == clima for h in lista):
                        if animal.habitat == habitat:
                            if any(alimento in animal.alimentacion for h in lista if
                                   h.tipo == habitat and h.clima == clima for alimento in h.alimentacion):
                                if any(h.capacidad != 0 for h in lista if h.tipo == habitat and h.clima == clima):
                                    for h in lista:
                                        if h.tipo == habitat and h.clima == clima and h.capacidad != 0:
                                            h.capacidad -= 1
                                            if h in self.asignacion:
                                                self.asignacion[h].append(animal)
                                            else:
                                                self.asignacion[h] = [animal]
                                            print("El animal fue asignado exitosamente al habitat\n")
                                            break
                                else:
                                    print("No hay capacidad para ingresar este animal\n")
                            else:
                                print("La dieta de este animal no es optima para este habitat\n")
                        else:
                            print("Ese no es el habitat de origen del animal, podria ser perjudicial para su salud\n")
                    else:
                        print("No coincide el clima con los tipos que hay\n")
                else:
                    print("Ese habitat no esta en lista del mismo tipo\n")
            else:
                print("Ese Habitat no existe\n")
        else:
            print("Ese animal no se encuentra registrado en el Zoologico\n")

    def agregar_alimentos(self, dieta, alimentos):
        if dieta not in self.alimentacion:
            self.alimentacion[dieta] = []

        self.alimentacion[dieta].append(alimentos)




    def mostrar_asignados(self):
        for habitat, animales in self.asignacion.items():
            print( f"Habitat: {habitat.tipo} de Clima:{habitat.clima} y Temperatura de: {habitat.temperatura} con una Humedad: {habitat.humedad}")
            print("Animales agregados: ")
            for animal in animales:
                print(animal.nombre, end=", ")
        print("\n")

    def catologo_animales(self):
        with st.container:
            st.subheader("Todos los animales:")
            if len(self.animales) == 0:
                st.error("No hay animales")
            else:
                for key, animal in self.animales.items():
                    st.markdown(f'**:red[id del animal:]**{key} **:red[Nombre:]**{animal.nombre} **:red[Especie:]** {animal.especie}')


    def devuelve(self):
        return self.habitats

