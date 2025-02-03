# finger 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
# read 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
# finguer1 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

import streamlit as st
import requests

# Configurar API de Hugging Face
API_URL = "https://api-inference.huggingface.co/models/tiiuae/falcon-7b-instruct"  # Cambia el modelo si es necesario
#API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large"

HEADERS = {"Authorization": "Bearer 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"}  # Reemplaza con tu API Key de Hugging Face


st.title("🤖 Chat con Hugging ")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

user_input = st.chat_input("Escribe tu mensaje aquí...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("user"):
        st.markdown(user_input)

    with st.chat_message("assistant"):
        with st.spinner("Pensando..."):
            response = requests.post(API_URL, headers=HEADERS, json={"inputs": user_input})

            try:
                # 📌 Extraer solo la parte relevante de la respuesta
                raw_reply = response.json()[0]["generated_text"]
                result = raw_reply.split("\n")[-1].strip()  # Extrae solo el resultado numérico
                formatted_reply = f"La respuesta es:  {result}"  # Espacio extra después de ":"
            except (KeyError, IndexError):
                formatted_reply = "❌ No se encontró una respuesta válida."

            st.markdown(formatted_reply)
            st.session_state.messages.append({"role": "assistant", "content": formatted_reply})
