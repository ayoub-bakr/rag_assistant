from app.services.document_loader import DocumentLoader
from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService


def main():

    # Load all documents
    loader = DocumentLoader()
    documents = loader.load_all_documents()

    print(f"Loaded Documents: {len(documents)}")

    # Chunk documents
    chunk_service = ChunkService(
        chunk_size=1000,
        chunk_overlap=200,
    )

    chunks = chunk_service.split_documents(documents)

    print(f"Generated Chunks: {len(chunks)}")

    # Generate embeddings
    embedding_service = EmbeddingService()

    embeddings = embedding_service.embed_chunks(chunks)

    print(f"Generated Embeddings: {len(embeddings)}")

    # Check first embedding
    if embeddings:
        print("=" * 80)
        print(f"Chunk ID          : {embeddings[0].chunk_id}")
        print(f"Vector dimension  : {len(embeddings[0].vector)}")
        print(f"First 5 values    : {embeddings[0].vector[:5]}")


if __name__ == "__main__":
    main()