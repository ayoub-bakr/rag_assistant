from dataclasses import dataclass, field
from typing import Any

@dataclass(slots=True)
class Document:
    """
    Represents a document loaded from the data source.
    """

    id: str
    file_name: str
    text: str
    metadata: dict[str, Any] = field(default_factory=dict)