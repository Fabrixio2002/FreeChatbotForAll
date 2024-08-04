# Chatbot con Flask y NLTK

Este proyecto consiste en la implementación de un chatbot utilizando Flask para el backend y NLTK para el procesamiento del lenguaje natural. El chatbot es capaz de responder a preguntas frecuentes, enviar documentos PDF, y gestionar nuevas preguntas y respuestas a través de una interfaz de contacto que permite a los estudiantes agregar sus preguntas.

## Contenido
- [Instalación](#instalación)
- [Configuración](#configuración)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Descripción de Archivos](#descripción-de-archivos)
- [Funcionalidades](#funcionalidades)
- [Uso](#uso)
- [Ejemplo de Uso](#ejemplo-de-uso)
- [Contacto](#contacto)

## Instalación

Para poner en marcha este proyecto, sigue los siguientes pasos:

1. Clonar el repositorio:

    ```bash
    git clone https://github.com/tu-usuario/chatbot-flask-nltk.git
    cd chatbot-flask-nltk
    ```

2. Crear un entorno virtual e instalar dependencias:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Descargar recursos de NLTK:

    En `index.py`, ya se incluyen las instrucciones para descargar los recursos necesarios de NLTK:

    ```python
    import nltk
    nltk.download('punkt')
    nltk.download('averaged_perceptron_tagger')
    ```

## Configuración

Asegúrate de tener los archivos necesarios en las rutas correctas. El archivo `intents.json` debe estar en la raíz del proyecto y los documentos PDF deben estar en el directorio `documentos/`.

## Estructura del Proyecto

```plaintext
chatbot-flask-nltk/
├── documentos/
│   └── Computacion.pdf
├── static/
│   ├── css/
│   │   ├── contacto.css
│   │   └── styles.css
│   └── img/
│       ├── fondo.png
│       ├── fondowt.jpg
│       ├── Logo_uth_normal.png
│       ├── logo2.png
│       ├── logo2white.png
│       ├── logouth.png
│       └── uth2.png
├── templates/
│   ├── contacto.html
│   └── index.html
├── intents.json
├── index.py
└── requirements.txt
```
## Descripción de Archivos

- **index.py**: Contiene la lógica principal del chatbot y la configuración de Flask.
- **intents.json**: Archivo JSON con las intenciones del chatbot, patrones y respuestas.
- **templates/**: Directorio que contiene las plantillas HTML para las diferentes rutas de la aplicación.
  - **index.html**: Página principal donde los usuarios pueden interactuar con el chatbot.
  - **contacto.html**: Página de contacto donde los estudiantes pueden agregar nuevas preguntas.
- **static/**: Directorio que contiene archivos estáticos como CSS e imágenes.
  - **css/**: Estilos CSS para las diferentes páginas.
  - **img/**: Imágenes utilizadas en la aplicación.
- **documentos/**: Directorio que contiene los documentos PDF que el chatbot puede enviar.
- **requirements.txt**: Archivo que lista todas las dependencias del proyecto.
- **README.md**: Este archivo proporciona una guía detallada sobre el proyecto.

## Funcionalidades

- **Respuesta a Preguntas Frecuentes**: El chatbot puede responder a preguntas comunes basadas en patrones definidos en `intents.json`.
- **Envío de Documentos**: Si se solicita un documento específico, el chatbot puede enviar un archivo PDF.
- **Gestión de Preguntas y Respuestas**: A través de la página de contacto, los estudiantes pueden agregar nuevas preguntas, las cuales se almacenan en `intents.json` para su posterior respuesta.

## Uso

1. Ejecutar la aplicación:

    ```bash
    python index.py
    ```

2. Acceder a la aplicación:

    Abre un navegador y ve a [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

3. Interacción con el Chatbot:

    En la página de inicio, puedes interactuar con el chatbot y recibir respuestas automáticas. En la página de contacto, puedes agregar nuevas preguntas que serán registradas en `intents.json`.

## Ejemplo de Uso

**Interacción Básica**

- **Usuario**: "Hola"
- **Chatbot**: "¡Hola! ¿Cómo estás?"

**Solicitud de Documentos**

- **Usuario**: "¿Qué clases lleva ingeniería en computación?"
- **Chatbot**: Envío del archivo `Computacion.pdf`.

**Gestión de Preguntas Frecuentes**

- **Estudiante**: Añadir una nueva pregunta a través de la página de contacto, que será almacenada para su futura respuesta.






