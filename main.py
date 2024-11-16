import streamlit as st
from funciones import obtener_respuesta_openai


st.image("images/banner.png")

# Inicializar el historial en st.session_state si no existe con el mensaje de bienvenida
if "historial" not in st.session_state:
    st.session_state.historial = [
        {"role": "assistant", "content": "¡Hola! Soy CableBot, ¿en qué puedo ayudarte hoy?"}
    ]

# Display chat messages from history on app rerun
for message in st.session_state.historial:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("Preguntame lo que quieras"):
    # Add user message to chat history
    # st.session_state.historial.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Display user message in chat message container
    with st.spinner('Espera un instante'):
        respuesta = obtener_respuesta_openai(prompt)
    with st.chat_message("assistant"):
        st.markdown(respuesta)
