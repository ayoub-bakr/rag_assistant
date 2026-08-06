from app.services.document_loader import DocumentLoader
from app.services.chunk_service import ChunkService


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

    print(f"Generated Chunks: {len(chunks)}\n")

    # Print chunks
    for chunk in chunks:
        print("=" * 80)
        print(f"Chunk ID      : {chunk.id}")
        print(f"Document ID   : {chunk.document_id}")
        print(f"Source        : {chunk.metadata.get('source')}")
        print(f"Length        : {len(chunk.text)}")
        print("-" * 80)
        print(chunk.text[:200])   # أول 200 حرف
        print()


if __name__ == "__main__":
    main()