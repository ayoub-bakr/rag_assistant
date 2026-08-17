from langchain_core.documents import Document as LangChainDocument
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.models.document import Document
from app.models.chunk import Chunk

class ChunkService:
    """
    Split documents into overlapping chunks using Langchain
    """
    def __init__(self,
                 chunk_size: int = 1000,
                 chunk_overlap: int = 200
                 ):
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
            length_function=len,
        )

    def split_documents(self, documents: list[Document]) -> list[Chunk]:

        chunks = []
        

        for document in documents:

            langchain_doc = LangChainDocument(
                page_content=document.text,
                metadata=document.metadata,
            )
            split_docs = self.text_splitter.split_documents([langchain_doc])
            for index, split_doc in enumerate(split_docs, start=1):
                chunks.append(
                    Chunk(
                        id=f"{document.id}-{index}",
                        document_id=document.id,
                        text=split_doc.page_content,
                        chunk_index=index,
                        metadata=split_doc.metadata,
                    )
                )

        return chunks