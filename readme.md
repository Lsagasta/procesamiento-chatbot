# **Chatbot RAG para Distribuidora de Insumos Eléctricos**

![Badge: Streamlit](https://img.shields.io/badge/Framework-Streamlit-red) 
![Badge: LangChain](https://img.shields.io/badge/NLP-LangChain-blue) 
![Badge: Pinecone](https://img.shields.io/badge/Embeddings-Pinecone-green) 
![Badge: OpenAI](https://img.shields.io/badge/API-OpenAI-lightblue) 

## **Descripción del Proyecto**
Este chatbot está diseñado para operar como un sistema RAG (Retrieval-Augmented Generation), utilizando como base de conocimiento cualquier archivo proporcionado por el usuario. Actualmente, se utiliza la información de una empresa ficticia que distribuye insumos eléctricos.  

### **Funcionalidades principales**  
- **Consulta de productos:** características, precios y presentaciones disponibles.  
- **Información sobre la empresa:** historia, sucursales y métodos de entrega.  
- **Adaptabilidad:** permite configurar una base de conocimiento personalizada cargada a Pinecone.  

### **Tecnologías utilizadas**
- **LangChain:** para la integración del flujo conversacional.  
- **OpenAI:** generación de respuestas utilizando GPT.  
- **Pinecone:** para almacenar y buscar embeddings de los documentos.  
- **Streamlit:** interfaz interactiva y amigable para el usuario.  

---

## **Instrucciones para Hacerlo Funcionar**

### **1. Prerrequisitos**  
- Python 3.9+  
- Tener configurados servicios externos como OpenAI y Pinecone.  
- Subir la base de conocimiento a Pinecone (pronto se publicará un repositorio adicional para facilitar este proceso).  

### **2. Instalación de Dependencias**  
1. Crea un entorno virtual:  
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows usa: venv\Scripts\activate

2. Instala las dependencias
    ```bash
    pip install -r requirements.txt

### **3. Configuración de Variables de Entorno**

1. En la raíz del proyecto, crea una carpeta llamada .streamlit.

2. Dentro de esta carpeta, crea un archivo secrets.toml con el siguiente formato:
    ```toml
    OPENAI_API_KEY = "tu_api_key"
    PINECONE_API_KEY = "tu_api_key"

### **4. Ejecución del Chatbot**

Una vez instaladas las dependencias y configuradas las variables:
    ```bash
    streamlit run main.py

Esto abrirá la aplicación en tu navegador por defecto.


### **Contacto**
Para dudas o consultas, podés contactarme:

**Correo**: lucas.sagasta@gmail.com








