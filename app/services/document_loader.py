from pathlib import Path

from app.models.document import Document


class DocumentLoader:
    """
    Load all text documents from the data directory.
    """

    def __init__(self, data_dir: str = "data/raw"):
        self.file_dir = Path(data_dir)

    def load_all_documents(self) -> list[Document]:

        documents = []

        if not self.file_dir.exists() or not self.file_dir.is_dir():
            raise FileNotFoundError(
                f"Directory '{self.file_dir}' does not exist."
            )

        for file_path in sorted(self.file_dir.glob("*.txt")):

            text = file_path.read_text(encoding="utf-8")

            documents.append(
                Document(
                    id=file_path.stem,
                    file_name=file_path.name,
                    text=text,
                    metadata={
                        "source": file_path.name
                    }
                )
            )

        return documents