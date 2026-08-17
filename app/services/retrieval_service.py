import numpy as np 

from sentence_transformers import SentenceTransformer
from app.storage.json_store import json_store

class RetrievalService:
    """
    Retrieve relevant chunks based on embeddings using a local BGE-M3 model.
    """
    def __init__(
            self,
            model_path: str = "/home/domapp/AiWork/models/bge-m3",
            store=None
    ):
        self.embedding_model = SentenceTransformer(model_path)
        self.store = store or json_store
 