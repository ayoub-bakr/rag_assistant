from pathlib import Path


class DocumentLoader:
    """Load all text documents from the data directory."""

    def __init__(self, data_dir: str = "data/raw"):
        self.file_dir = Path(data_dir)

    def load_all_documents(self):
        """Load all text documents from the data directory.

        Returns:
            list[dict]: A list of document metadata dictionaries with keys
                'id', 'file_name', 'text', and 'metadata'.
        """
        documents = []
        if not self.file_dir.exists() or not self.file_dir.is_dir():
            raise FileNotFoundError(f"Directory '{self.file_dir}' does not exist.")

        for file_path in self.file_dir.glob("*.txt"):

            text = file_path.read_text(encoding="utf-8")

            from app.models.document import Document

        return documents
