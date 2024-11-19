import streamlit as st
from pinecone import Pinecone
from langchain.embeddings.openai import OpenAIEmbeddings
import openai

# --- CONFIGURO LAS CONEXIONES A LA DB Y AL LLM ---

# Obtengo key de openai
openai.api_key = st.secrets["OPENAI_API_KEY"]
# Defino el modelo de embeddings de OpenAI
embeddings = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=3072)

# Instancio un objeto Pinecone
pc = Pinecone(api_key=st.secrets["PINECONE_API_KEY"])
# Defino el nombre de la base de datos
index_name = "cablepro-chabot"
# Conectar al índice existente
index = pc.Index(index_name)


# ----------- DEFINO FUNCIONES --------------

# Genero una función para obtener un embedding a partir de una pregunta
def obtener_embedding(pregunta):
    embedding = embeddings.embed_query(pregunta)
    return embedding

# (deprecar si funciona el session state)
# Inicializa una lista global para el historial de mensajes
# historial = []


def obtener_respuesta_openai(pregunta: str, top_k=5):

    # 1. Obtener el embedding de la pregunta
    embedding_pregunta = obtener_embedding(pregunta)

# 2. Buscar los vectores más similares en Pinecone
    response = index.query(vector=embedding_pregunta,
                           top_k=top_k, include_metadata=True)

# 3. Extraer los documentos más relevantes (suponiendo que los metadatos contienen los textos)
    documentos_relevantes = [match.get('metadata', {}).get(
        'text', '') for match in response['matches']]

# 4. Crear un contexto a partir de los documentos relevantes
    contexto = "\n".join(documentos_relevantes)
    pregunta_and_contexto = {"role": "user", "content": f"Pregunta: {
        pregunta}\n\nContexto:\n{contexto}"}

    # Mantén solo los últimos N mensajes para evitar sobrecargar el modelo
    N = 10  # Ajusta este valor según la cantidad de memoria que quieras mantener
    st.session_state.historial = st.session_state.historial[-N:]

    # Formatear el historial como texto para incluirlo en el mensaje del sistema
    historial_texto = "\n".join([f"{mensaje['role']}: {
                                mensaje['content']}" for mensaje in st.session_state.historial])

    # 5. Obtener la respuesta de OpenAI usando el historial
    respuesta_openai = openai.chat.completions.create(
        model="gpt-3.5-turbo-0125",  # Modelo a usar
        messages=[
            {"role": "system",
             "content": f"""
                 Eres un asistente útil para la empresa CablePro, especializada en la venta de cables y productos eléctricos.
                 Si un cliente pregunta por un producto o servicio relacionado con el mundo eléctrico pero que no vendemos específicamente,
                 dile que atenderás su consulta con gusto. Si el producto o servicio está fuera de contexto o no lo ofrecemos,
                 informa amablemente que no puedes ayudar con esa solicitud. Solo responde con información sobre los productos y servicios
                 disponibles en CablePro o relacionados con el mundo eléctrico.
                 Ten en cuenta el siguiente historial de mensajes anteriores y utilízalos como memoria:{historial_texto}"""}
        ] + [pregunta_and_contexto],  # Agrega el historial completo
        max_tokens=1500,  # Ajusta según lo que necesites
        temperature=0.1
    )
    # Obtén la respuesta del modelo
    respuesta = respuesta_openai.choices[0].message.content.strip()
    respuesta = respuesta.replace("$", "\\$")

    # Agrega el nuevo mensaje del usuario al historial
    st.session_state.historial.append({"role": "user", "content": pregunta})

    # Agrega la respuesta al historial
    st.session_state.historial.append(
        {"role": "assistant", "content": respuesta})

    return (respuesta)
