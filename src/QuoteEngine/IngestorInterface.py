import os
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

extensions = ['.txt', '.csv', '.pdf', '.docx']


class IngestorInterface(ABC):

    @classmethod
    def can_ingest(cls, path) -> bool:
        filename, file_extension = os.path.splitext(path)
        if file_extension in extensions:
            return True
        else:
            return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        pass
