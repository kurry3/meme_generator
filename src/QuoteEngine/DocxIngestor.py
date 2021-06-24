"""Docx Ingestor.

This script requires that the 'typing', 'os', and 'docx'
libraries be installed within the Python environment this script
is being run in.
"""

from typing import List
import docx
import os

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    """A class used if the input file has the extension .docx.

    It realizes the IngestorInterface.

    ...

    Methods:
        can_ingest(path): Returns the boolean value 'True' if the input file
            can be read and 'False' if not.
        parse(path=str): Returns a list of QuoteModels.
    """

    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of QuoteModels.

        Arguments:
            path{[str]}: the path where the file to be read is located
        Raises:
            Exception: if the file at the path is not of the correct format
                or if the .docx file at the path cannot be read
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        try:
            quotes = []
            path = path.replace('./', '')
            root = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(root, path).replace('\\', '/')
            doc = docx.Document(path)

            for para in doc.paragraphs:
                if para.text != "":
                    parse = para.text.replace(u"\u2019", "'").split(' - ')
                    new_quote = QuoteModel(parse[0], parse[1])
                    quotes.append(new_quote)
        except Exception as e:
            raise Exception(".docx parsing issue occurred.")
        return quotes
