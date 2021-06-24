"""Text Ingestor.

This script requires that the 'typing' and 'os' libraries
be installed within the Python environment this script
is being run in.
"""

import os
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    """A class used if the input file has the extension .txt.

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
                    or if the .txt file at the path cannot be read
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        path = path.replace('./', '')
        root = os.path.dirname(os.path.dirname(__file__))
        mod_path = os.path.join(root, path).replace('\\', '/')
        try:
            with open(mod_path, 'r', encoding='utf-8-sig') as f:
                for line in f:
                    one_line = line.strip('\n').replace(u"\u2019",
                                                        "'").split(' - ')
                    new_quote = QuoteModel(one_line[0], one_line[1])
                    quotes.append(new_quote)
        except Exception as e:
            raise Exception(".txt parsing issue occurred.")
        return quotes
