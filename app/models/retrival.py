from dataclasses import dataclass, field
from typing import Any 

from app.models.chunk import Chunk
from app.models.embedding import Embedding 

class Retrival:
    """
    Represents a retrieval result containing a chunk and its associated embedding.
    """

    def __init__(
            self, chunk: 'Chunk',
            embedding: 'Embedding'
            ):
        self.chunk = chunk
        self.embedding = embedding