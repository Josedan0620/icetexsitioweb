import streamlit as st

def main():
    st.title("Aplicación de ejemplo")
    st.write("¡Hola, bienvenido a Streamlit!")

    # Agregar elementos interactivos
    nombre = st.text_input("Ingresa tu nombre")
    st.write(f"Hola {nombre}!")

    edad = st.slider("Ingresa tu edad", 0, 100, 25)
    st.write(f"Tienes {edad} años")

    colores = ["Rojo", "Verde", "Azul"]
    color_seleccionado = st.selectbox("Elige un color", colores)
    st.write(f"Has seleccionado el color {color_seleccionado}")

    if st.button("¡Haz clic aquí!"):
        st.write("¡Botón presionado!")

if __name__ == "__main__":
    main()






 





    
