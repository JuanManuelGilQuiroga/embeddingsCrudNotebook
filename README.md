## Sistema CRUD para Embeddings

### Introducción

Este repositorio contiene un Jupyter Notebook que implementa un sistema CRUD (Create, Read, Update, Delete) para trabajar con embeddings de texto. Utilizando la librería Sentence Transformers para generar embeddings, este proyecto proporciona una base sólida para realizar tareas de búsqueda semántica y análisis de texto.

### Requisitos

* **Python:** Versión 3.6 o superior.
* **Librerías:**
  * `Qdrant`: Una base de datos vectorial para almacenamiento y búsqueda de embeddings.
  * `Streamlit`: Una interfaz web interactiva para gestionar los embeddings.
  * `sentence-transformers`: Un modelo de machine learning para generar embeddings a partir de texto.

Para instalar las dependencias, ejecuta el siguiente comando en tu terminal:

```bash
pip install -r requirements.txt
```

### Estructura del proyecto
* **notebook.ipynb**: Contiene el código principal del proyecto, incluyendo la definición de la clase CRUD y ejemplos de uso.

### Uso del Proyecto

Guarda el archivo de la aplicación con el nombre app.py y ejecútala con:


```bash
streamlit run app.py
```

### Explicación de las funcionalidades

### Clase `EmbeddingCRUD`

Esta clase encapsula las operaciones CRUD sobre los embeddings:

#### 1. Constructor __init__()

Inicializa la instancia de la clase, configurando el cliente Qdrant, el modelo de embeddings y verificando si la colección existe.

```bash
self__init__(self):
```

self.model: Carga el modelo de sentence-transformers.

self.client: Inicializa la conexión con Qdrant.

self.index_name: Define el nombre de la colección en la base de datos.

self._initialize_collection(): Llama a la función para crear/verificar la colección.

#### 2. Metodo _initialize_collection()

Crea la colección en QDrant si no existe.

```bash
def _initialize_collection(self):
```

- Verificacion: Si la coleccion existe, la utiliza, de lo contrario la crea.

- Parametros del vector: Define la dimension y la metrica de distancia(coseno).


#### 3. Metodo id_generation()

Genera un identificador unico para cada embedding.

```bash
def id_generation(self)
```

- Retorna un numero aleatorio de 4 digitos entre 1000 y 9999


#### 4. Metodo create(text)

Crea un nuevo embedding a partir de un texto proporcionado.

```bash
def create(self, text):
```

- Entrada: text (cadena de texto)

- Salida: Retorna el ID generado y el embedding creado.

- Proceso:
 1. Convierte el texto en un embedding.
 2. Genera un ID unico.
 3. Almacena en la base de datos.


#### 5. Metodo read()

Recupera todos los embeddings almacenados en la base de datos.

```bash
def read(self):
```

- Salida: Lista de embeddings con su ID y texto asociado.

- Proceso:
 1. Realiza una consulta de lectura usando "scroll".
 2. Devuelve los resultados en forma de lista.


#### 6. Metodo read_similarity(text_query, top_k=5)

Busca embeddings similares a un texto proporcionado.

```bash
def read_similarity(self, text_query, top_k=5):
```

- Entrada:
 1. text_query: El texto a buscar.
 2. top_k: Numero de resultados mas similares (por defecto 5).

- Salida: Lista con los IDs, textos y puntajes de similitud.


#### Metodo update(id, new_text)

Actualiza un embedding existente con un texto.

```bash
def update(self, id, new_text):
```

- Entrada:
 1. id: ID del embedding a actualizar.
 2. new_text: Nuevo texto a almacenar.

- Proceso:
 1. Genera un nuevo embedding a partir del nuevo texto.
 2. Sobreescribe el registro con el nuevo valor.


#### 8. Metodo delete(id)

Elimina un embedding por su ID.

```bash
def delete(self, id):
```

- Entrada:
 1. id: ID del embedding a actualizar.
 2. Salida: Confirmacion de eliminación.

- Salida: Confirmacion de eliminacion.


### Base de datos vectorial

En este proyecto, utilizamos un DataFrame de Pandas como una base de datos vectorial simplificada. Cada fila del DataFrame representa un embedding y contiene el texto original y el vector numérico.

### Uso del notebook
 1. Abre el notebook en Jupyter Notebook.
 2. Ejecuta las celdas una por una para crear embeddings, realizar búsquedas y modificar los datos.
 3. Experimenta con diferentes textos y consultas para explorar las capacidades del sistema.

 ---

 ## ¿Qué son los embeddings?

 Los embeddings son representaciones numéricas de palabras, frases o documentos en un espacio vectorial de alta dimensión. Imagina cada palabra como un punto en un mapa multidimensional. Palabras con significados similares estarán cerca unas de otras en este mapa.

 ### ¿Para qué sirven?

 Los embeddings permiten a las computadoras entender y procesar el lenguaje de manera más similar a los humanos. Se utilizan en diversas tareas como:

 * **Búsqueda semántica**: Encontrar documentos similares a una consulta dada.
 * **Clasificación de texto**: Categorizar textos en diferentes temas.
 * **Traducción automática**: Alinear palabras y frases en diferentes idiomas.
 * **Recomendación de productos**: Sugerir productos relevantes a un usuario.

 ---

 ## Imagenes de uso - Notebook

 ![Crear Embedding](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/crearEmbedding.png)
 ![Buscar Embeddings](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/leerEmbeddings.png)
 ![Buscar Embedding Similar](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/BuscarEmbeddingsSimilares.png)
 ![Actualizar Embedding](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/ActualizarEmbedding.png)
 ![Eliminar Embedding](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/EliminarEmbedding.png)

 ## Imagenes de uso - FrontEnd
 ![Crear Embedding en FrontEnd](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/crearEmbeddingFrontend.png)
 ![Buscar Embeddings en FrontEnd](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/leerEmbeddingsFrontend.png)
 ![Buscar Embedding Similar en FrontEnd](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/buscarEmbeddingsSimilaresFrontend.png)
 ![Actualizar Embedding en FrontEnd](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/ActualizarEmbeddingFrontend.png)
 ![Eliminar Embedding en FrontEnd](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/eliminarEmbeddingFrontend.png)