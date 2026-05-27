import streamlit as st
st.title("Filtro de Seguridad por Edad")
edad = st.number_input("Introduce tu edad:", min_value=0, max_value=120, value=18)
if st.button("Verificar acceso"):
    if edad >= 18:
        st.success("¡Acceso concedido! Eres mayor de edad.")
    else:
        st.error("Acceso denegado. No se permiten menores de 18 años.")
