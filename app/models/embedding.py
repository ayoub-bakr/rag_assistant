from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class Embedding:
    """
    Represents an embedding vector associated with a document or chunk.
    """

    chunk_id: str
    vector: list[float]
    metadata: dict[str, Any] = field(default_factory=dict)