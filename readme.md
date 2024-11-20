# **Chatbot RAG para Distribuidora de Insumos Eléctricos**

![Badge: Streamlit](https://img.shields.io/badge/Framework-Streamlit-red) 
![Badge: LangChain](https://img.shields.io/badge/NLP-LangChain-blue) 
![Badge: Pinecone](https://img.shields.io/badge/Embeddings-Pinecone-green) 
![Badge: OpenAI](https://img.shields.io/badge/API-OpenAI-lightblue) 


## **Descripción del Proyecto**
Este chatbot está diseñado para operar como un sistema RAG (Retrieval-Augmented Generation), utilizando como base de conocimiento cualquier archivo proporcionado por el usuario. Actualmente, se utiliza la información de una empresa ficticia que distribuye insumos eléctricos.  

<img width="4688" alt="flujo" src="https://github.com/user-attachments/assets/611b4c59-b2c8-4811-8965-66d8a3e50e02">

### **Funcionalidades principales**  
- **Consulta de productos:** características, precios y presentaciones disponibles.  
- **Información sobre la empresa:** historia, sucursales y métodos de entrega.  
- **Adaptabilidad:** permite configurar una base de conocimiento personalizada cargada a Pinecone.  

### **Tecnologías utilizadas**
- **LangChain:** para la integración del flujo conversacional.  
- **OpenAI:** generación de respuestas utilizando GPT.  
- **Pinecone:** para almacenar y buscar embeddings de los documentos.  
- **Streamlit:** interfaz interactiva y amigable para el usuario.

<img width="3600" alt="tecnicas" src="https://github.com/user-attachments/assets/72f63930-e701-4763-9801-c4d01e08a77a">


---

## ¡Prueba el Proyecto en Vivo! 🚀

Podés visitar la versión desplegada del proyecto y probar todas sus funcionalidades en tiempo real. 

🔗 [Accede al proyecto aquí](https://cable-pro.streamlit.app/)

![screen](https://github.com/user-attachments/assets/e6d35776-eba7-4c8d-8a2f-8cb844e4d7d3)


Realizá todas las pruebas que desees. ¡Tu feedback es muy valioso para mí!


---

### **En caso de que desees clonar el proyecto:**

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


## Trabajo en Equipo 🤝  

Este proyecto no habría sido posible sin el talento y dedicación de un increíble equipo de trabajo. ¡Conoce a quienes hicieron esto realidad!  


|         |                                          |  |
|----------------------|------------------------------------------------------------|---------|
|**Damian Cardinaux** | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/damiancx/) | Data Scientist and AI Specialist|
|**Natalia Riera** | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/nataliariera/) | Data Scientist and AI Specialist |
|**Pablo Cardozo**    | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/pablo-cardozo16/) | Data Scientist and AI Specialist |
|**Lucas Sagasta**    | [![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue)](https://www.linkedin.com/in/lucas-sagasta-4291198b/) | Data Scientist and AI Specialist |

---

✨ **¡Gracias a todos por su dedicación y esfuerzo!** ✨




### **Contacto**
Para dudas o consultas, podés contactarme:

**Correo**: lucas.sagasta@gmail.com








