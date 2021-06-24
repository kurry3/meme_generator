import os
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .DocxIngestor import DocxIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        filename, file_extension = os.path.splitext(path)
        if file_extension == ".txt":
            return TextIngestor.parse(path)
        elif file_extension == ".docx":
            return DocxIngestor.parse(path)
        elif file_extension == ".pdf":
            return PDFIngestor.parse(path)
        elif file_extension == ".csv":
            return CSVIngestor.parse(path)
        else:
            raise ValueError("Unsupported file extension:", file_extension)
