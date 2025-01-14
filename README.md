## Sistema CRUD para Embeddings

### Introducción

Este repositorio contiene un Jupyter Notebook que implementa un sistema CRUD (Create, Read, Update, Delete) para trabajar con embeddings de texto. Utilizando la librería Sentence Transformers para generar embeddings y Pandas para almacenar y manipular los datos, este proyecto proporciona una base sólida para realizar tareas de búsqueda semántica y análisis de texto.

### Requisitos

* **Python:** Versión 3.6 o superior.
* **Librerías:**
  * `pandas`
  * `numpy`
  * `sentence-transformers`

Para instalar las dependencias, ejecuta el siguiente comando en tu terminal:

```bash
pip install pandas sentence-transformers numpy
```

### Estructura del proyecto
* **notebook.ipynb**: Contiene el código principal del proyecto, incluyendo la definición de la clase CRUD y ejemplos de uso.

### Explicación de las funcionalidades

### Clase `EmbeddingCRUD`

Esta clase encapsula las operaciones CRUD sobre los embeddings:

* **create(text)**: Crea un nuevo embedding para el texto dado, lo agrega al DataFrame y lo guarda.
* **read(query)**: Busca embeddings similares a una consulta dada. Calcula la similitud coseno entre la consulta y cada embedding almacenado y devuelve los resultados ordenados por similitud.
* **update(index, new_text)**: Actualiza el texto y el embedding de un registro específico.
* **delete(index)**: Elimina un registro del DataFrame.

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

 ## Imagenes de uso

 ![Crear Embedding](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/CrearEmbeddings.png)
 ![Buscar Embedding](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/BuscarEmbeddingsSimilares.png)
 ![Actualizar Embedding](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/ActualizarEmbedding.png)
 ![Eliminar Embedding](https://github.com/JuanManuelGilQuiroga/embeddingsCrudNotebook/blob/main/img/EliminarEmbedding.png)