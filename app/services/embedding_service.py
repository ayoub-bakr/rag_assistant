from sentence_transformers import SentenceTransformer

from app.models.chunk import Chunk
from app.models.embedding import Embedding


class EmbeddingService:
    """
    Generate embeddings for text chunks using a local BGE-M3 model.
    """

    def __init__(
        self,
        model_path: str = "/home/domapp/AiWork/models/bge-m3",
    ):
        self.embedding_model = SentenceTransformer(
            model_path
        )

    def embed_chunks(
        self,
        chunks: list[Chunk],
    ) -> list[Embedding]:

        texts = [chunk.text for chunk in chunks]

        vectors = self.embedding_model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            normalize_embeddings=True,
        )

        embeddings = []

        for chunk, vector in zip(chunks, vectors):
            embeddings.append(
                Embedding(
                    chunk_id=chunk.id,
                    vector=vector.tolist(),
                    metadata=chunk.metadata.copy(),
                )
            )

        return embeddings