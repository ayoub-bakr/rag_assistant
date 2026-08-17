import json 
from pathlib import Path
from typing import Any

class JsonStore:
    """
    Store and load embeddings records using Json files.
    """
    def __init__(self, file_path: str = "data/embeddings.json"):
        self.file_path = Path(file_path)