
from pydantic import BaseModel, Field
from typing import Any



class Document(BaseModel):
        id: str
        file_name: str
        text: str
        metadata: dict[str, Any] = Field(default_factory=dict)
