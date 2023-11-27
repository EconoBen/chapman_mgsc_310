"""Main module for the API"""
from qdrant_client import QdrantClient
from qdrant_client.http.models import Distance, VectorParams

client = QdrantClient("localhost", port=6333)

def set_collection():
    client.create_collection(
    collection_name="class_collection",
    vectors_config=VectorParams(size=4, distance=Distance.COSINE),
)



if __name__ == "__main__":
    

