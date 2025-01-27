from qdrant_client import QdrantClient
from sentence_transformers import SentenceTransformer
from qdrant_client.models import VectorParams, Distance
import random

class EmbeddingCRUD:
    def __init__(self):
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.client = QdrantClient(
            url="https://4715095d-53aa-4f96-8cfe-e542e53f8dd8.eu-west-2-0.aws.cloud.qdrant.io:6333", 
            api_key="2Md9iPHFRxTCSdr6a_tgQrk1BJaf2SAfzx6e9qvqaH7aDc-wogWwtw",
            https=True
        )
        self.index_name = "embeddings_index"

        self._initialize_collection()

    def _initialize_collection(self):
        try:
            # Verifica si la colección ya existe
            self.client.get_collection(self.index_name)
            print(f"La colección '{self.index_name}' ya existe.")
        except:
            print(f"Colección '{self.index_name}' no encontrada, creando...")

            self.client.create_collection(
                collection_name=self.index_name,
                vectors_config=VectorParams(
                    size=self.model.get_sentence_embedding_dimension(),
                    distance=Distance.COSINE  # Se usa distancia de coseno para la similitud
                )
            )
            print(f"Colección '{self.index_name}' creada exitosamente.")

    def id_generation(self):
        return random.randint(1000, 9999)

    def create(self, text):
        embedding = self.model.encode([text])[0].tolist()
        new_id = self.id_generation()
        self.client.upsert(
            collection_name=self.index_name,
            points=[{
                'id': new_id,
                'vector': embedding,
                'payload': {'text': text}
            }]
        )
        return new_id, embedding

    def read(self):
        embeddings = []
        scroll_response = self.client.scroll(collection_name=self.index_name, limit=1000)

        while scroll_response and scroll_response[0]:
            for point in scroll_response[0]:
                embeddings.append({
                    'id': point.id,
                    'vector': point.vector if point.vector else [],
                    'payload': point.payload.get('text', '')
                })

            scroll_token = scroll_response[1]
            if not scroll_token:
                break
            
            scroll_response = self.client.scroll(collection_name=self.index_name, scroll_token=scroll_token)

        return embeddings

    def read_similarity(self, text_query, top_k=5):
        embedding_query = self.model.encode([text_query])[0]
        resultados = self.client.search(
            collection_name=self.index_name,
            query_vector=embedding_query.tolist(),
            limit=top_k
        )
    
        return [{
            "id": res.id,
            "text": res.payload["text"],
            "score": res.score
        } for res in resultados]
    
    def update(self, id, new_text):
        updated_embedding = self.model.encode([new_text])[0]
        self.client.upsert(
            collection_name=self.index_name,
            points=[{
                'id': id,
                'vector': updated_embedding.tolist(),
                'payload': {'text': new_text}
            }]
        )
        print(f"El texto en el id {id} ha sido actualizado a '{new_text}'")

    def delete(self, id):
        self.client.delete(
            collection_name=self.index_name,
            points_selector=[id]
        )
        print(f"Se ha eliminado el índice {id}")