from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class Chunk:
    """
       Represents a chunk of text extracted from a document.
    """

    id: str
    document_id: str
    text: str
    chunk_index: int
    metadata: dict[str, Any] = field(default_factory=dict)
    