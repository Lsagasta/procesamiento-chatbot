1. Crear entorno virtual 

python -m venv venv


2. Activar entorno virtual

.\venv\Scripts\activate

3. Instalar reqquerimientos.

pip install -r .\requirements.txt

4. crear una carpeta en la raiz del proyecto llamada: ".streamlit"

5. crear un archivo llamado secrets.toml y pegar tu api key de openai

OPENAI_API_KEY = "aca pega tu apikey"