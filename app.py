import streamlit as st
from CRUD import EmbeddingCRUD

crud = EmbeddingCRUD()

st.title("CRUD de Embeddings con Qdrant")

st.header("Crear un nuevo documento")
new_text = st.text_area("Ingrese el texto:")
if st.button("Crear"):
    if new_text:
        new_id, _ = crud.create(new_text)
        st.success(f"Documento creado con ID: {new_id}")
    else:
        st.error("Por favor ingrese un texto válido.")

st.header("Visualizar todos los documentos")
if st.button("Cargar documentos"):
    embeddings = crud.read()
    if embeddings:
        for doc in embeddings:
            st.write(f"ID: {doc['id']} - Texto: {doc['payload']}")
    else:
        st.warning("No hay documentos en la base de datos.")

st.header("Buscar similitud de documentos")
query_text = st.text_input("Ingrese el texto de búsqueda:")
if st.button("Buscar"):
    if query_text:
        resultados = crud.read_similarity(query_text)
        for res in resultados:
            st.write(f"ID: {res['id']} - Texto: {res['text']} - Similitud: {res['score']:.2f}")
    else:
        st.error("Ingrese un texto para buscar.")

st.header("Actualizar documento")
update_id = st.number_input("Ingrese el ID del documento a actualizar:", step=1, min_value=0)
update_text = st.text_area("Nuevo texto:")
if st.button("Actualizar"):
    if update_id and update_text:
        crud.update(update_id, update_text)
        st.success(f"Documento con ID {update_id} actualizado.")
    else:
        st.error("Ingrese un ID válido y un nuevo texto.")

st.header("Eliminar documento")
delete_id = st.number_input("Ingrese el ID del documento a eliminar:", step=1, min_value=0)
if st.button("Eliminar"):
    if delete_id:
        crud.delete(delete_id)
        st.success(f"Documento con ID {delete_id} eliminado.")
    else:
        st.error("Ingrese un ID válido.")
