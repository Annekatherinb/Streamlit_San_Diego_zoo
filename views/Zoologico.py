import models.Animal as animalModel
import models.Habitat as habitatModel
import models.BaseDatos as plataforma
import controllers.ZoologicoController as zooController
import streamlit as st
from streamlit_player import st_player

class Zoologico:

    def __init__(self, nombre):
        self. nombre = nombre
    def menu(self):
        base = plataforma.Datos()
        controlador = zooController.ZoologicoController(base, self)
        opcion1=0
        opcion2=0
        opcion3=0
        opcion4=0
        tab1, tab2, tab3, tab4 = st.tabs(["Pagina Principal", "Ingreso", "Caracteristicas habitat", "Catalogo del Zoologico"])
        with tab1:
            st.title('**Bienvenidos** 🦁')
            video_file = open('myvideo.mp4', 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)

        with tab2:
            st.header(':orange[**Formulario de Ingreso de animales**]')
            boton_ingreso = st.button("Diligenciar Formulario", 1)
            if boton_ingreso == True:
                st.session_state["opcion1"] = 1

            if "opcion1" in st.session_state:
                controlador.accion(st.session_state["opcion1"])

        with tab3:
            st.header(':blue[**Habitat**]')
            boton_habitat = st.button("Crear Habitat", key="butHabi")
            if boton_habitat:
                st.session_state["opcion3"] = 3
            if "opcion3" in st.session_state:
                controlador.accion(st.session_state["opcion3"])

        with tab4:
            st.header(':blue[**Catalogo Completo**]')
            animales = st.button("Todos los animales", key="clave animal")
            if animales:
                st.session_state["opcion2"] = 2

            if "opcion2" in st.session_state:
                controlador.accion(st.session_state["opcion2"])



    def menu_crearAnimal(self, id):
        st.subheader("Nombre")
        nombre = st.text_input("Ingrese el nombre del animal:")
        st.subheader("Especie")
        especie = st.text_input("Especie del animal:")
        st.subheader("Habitat:")
        pTempH = ['ninguna', 'selvatico', 'acuatico', 'desertico', 'polar', 'otro']
        habitat= st.radio('Selecciona una opción', pTempH, key="habitat")
        if habitat != 'ninguna':
            st.write('Has seleccionado:', habitat)
        else:
            st.write('No se ha seleccionado ningún hábitat.')

        if habitat == 'otro':
            habitat = st.text_input("Nombre del nuevo habitat:")

        st.subheader("Alimentacion:")
        pAlimento =  ['ninguna', 'herbivoro', 'carnivoro', 'omnivoro']
        alimentacion = st.radio('Selecciona una opción', pAlimento, key="alimento")
        if alimentacion != 'ninguna':
            st.write('Has seleccionado:', alimentacion)
        else:
            st.write('No se ha seleccionado ningún tipo de slimentacion.')

        st.subheader("Edad:")
        edad = st.number_input("Edad del animal:", min_value=1, max_value=200)

        st.subheader("Salud:")
        pSalud =  ['ninguna', 'estable', 'en revision', 'estado critico']
        salud = st.radio('Selecciona una opción',pSalud, key="salud")

        st.subheader("Horas de Sueño:")
        horasSueno = st.number_input("Horas que duerme el animal:", min_value=0, key="sueno")
        juego = 0
        boton_guardar=st.button("Guardar")
        if boton_guardar == True:
            nuevoAnimal = animalModel.Animal(id, nombre, especie, edad, habitat, alimentacion, salud, juego, horasSueno)
            st.success("Animal Añadido exitosamente")
            return nuevoAnimal


    def menu_habitat(self, tipo):

        st.subheader("Humedad:")
        humedad = st.radio("Niveles de humedad:", ["ninguna", "Alto", "Moderado", "Bajo"])

        if humedad!= 'ninguna':
            if humedad == "Alta":
                humedad = "alta"
            elif humedad == "Moderada":
                humedad = "moderada"
            elif humedad == "Baja":
                humedad = "baja"
            st.write('Has seleccionado:',humedad)
        else:
            st.write('No se ha seleccionado ningún tipo de slimentacion.')

        st.subheader("Clima:")
        clima = st.text_input("Qué clima tiene:", key="clima")

        while clima.isdigit():
            st.warning("Los caracteres ingresados no son válidos. Se requiere una cadena de texto.")
            clima = st.text_input("Qué clima tiene:")

        st.write("El clima ingresado es:", clima)

        st.subheader("Temperatura:")
        temperatura = st.text_input("Digite el valor de la temperatura:", key="temperatura")

        st.write("El valor de la temperatura ingresado es:", temperatura)

        st.subheader("Capacidad:")
        capacidad = st.number_input("cantidad max de animales:", min_value=1, max_value=5)
        st.write("El numero de animales que puede albergar es:", capacidad)

        st.subheader("Alimentacion:")
        lista_comida = st.multiselect("Seleccione las dietas permitidas:",
                                      ["herbivoro", "carnivoro", "omnivoro"])

        st.write("Los alimentos seleccionados son:")
        st.write(lista_comida)

        boton_crear_habitat = st.button("Crear")
        if boton_crear_habitat == True:
            nuevoHabitat = habitatModel.Habitat(tipo, humedad, clima, temperatura, capacidad, lista_comida)
            st.success("Habitat Habilitada existosamente")
            return nuevoHabitat

    def solicitar_animal(self, mensaje):
        return input(mensaje)

