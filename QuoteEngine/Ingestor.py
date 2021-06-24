"""Ingestor.

This script requires that the 'typing' and 'os'
libraries be installed within the Python environment this script
is being run in.
"""

import os
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface
from .CSVIngestor import CSVIngestor
from .PDFIngestor import PDFIngestor
from .DocxIngestor import DocxIngestor
from .TextIngestor import TextIngestor


class Ingestor(IngestorInterface):
    """A class that calls one IngestorInterface inheriting class.

    It realizes the IngestorInterface.

    ...

    Methods:
        can_ingest(path): Returns the boolean value 'True' if the input file
            can be read and 'False' if not.
        parse(path=str): Returns a list of QuoteModels.
    """

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of QuoteModels.

        Selects which Ingestor sub-module to call according to the
        file extension.

        Arguments:
            path{[str]}: the path where the file to be read is located
        Raises:
            Exception: if the file at the path is not of the correct format
        """
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
