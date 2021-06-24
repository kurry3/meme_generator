"""PDF Ingestor.

This script requires that the 'typing, 'os', and 'subprocess'
libraries be installed within the Python
environment this script is being run in.
"""

import os
import subprocess
import random
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    """A class used if the input file has the extension .pdf.

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

        Arguments:
            path{[str]}: the path where the file to be read is located
        Raises:
            Exception: if the file at the path is not of the correct format
                or if the .pdf file at the path cannot be read
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        try:

            path = path.replace('./', '')
            root = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(root, path).replace('\\', '/')
            tmp = f'_data/DogQuotes/{random.randint(0, 250)}.txt'
            root = os.path.dirname(os.path.dirname(__file__))
            tmp = os.path.join(root, tmp).replace('\\', '/')

            call = subprocess.call(['pdftotext', path, tmp])
            quotes = []
            with open(tmp, "r") as f:
                for line in f:
                    one_line = line.strip('\n').replace(u"\u2019",
                                                        "'").split(' - ')
                    new_quote = QuoteModel(one_line[0], one_line[1])
                    quotes.append(new_quote)
            os.remove(tmp)
        except Exception as e:
            raise Exception(".pdf parsing issue occurred.")

        return quotes
