class CRUD:
    def __init__(self, collection):
        self.collection = collection

    def create(self, embedding, metadata):
        self.collection.add(
            embeddings=[embedding],
            metadatas=[metadata]
        )
        print("Registro creado exitosamente.")

    def read(self, query_embedding, n_results=5):
        results = self.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results
        )
        return results

    def update(self, id, new_embedding, new_metadata):
        # Primero eliminamos el registro existente
        self.collection.delete(ids=[id])
        # Luego lo insertamos nuevamente con los nuevos datos
        self.create(new_embedding, new_metadata)
        print("Registro actualizado exitosamente.")

    def delete(self, id):
        self.collection.delete(ids=[id])
        print("Registro eliminado exitosamente.")

# Ejemplo de uso
if __name__ == "__main__":
    from chromadb.db import Chroma

    # Crear una instancia de Chroma y una colección
    chroma = Chroma(persist_directory="./chroma_db")
    collection = chroma.create_collection("my_collection")

    # Crear una instancia de la clase CRUD
    crud = CRUD(collection)

    # Crear un nuevo registro
    embedding = [0.1, 0.2, 0.3]
    metadata = {"text": "Este es un nuevo registro"}
    crud.create(embedding, metadata)

    # Leer registros similares
    query_embedding = [0.15, 0.25, 0.35]
    results = crud.read(query_embedding)
    print(results)

    # Actualizar un registro (suponiendo que conoces el ID)
    id_a_actualizar = results["matches"][0]["id"]
    new_embedding = [0.4, 0.5, 0.6]
    new_metadata = {"text": "Texto actualizado"}
    crud.update(id_a_actualizar, new_embedding, new_metadata)

    # Eliminar un registro
    crud.delete(id_a_actualizar)