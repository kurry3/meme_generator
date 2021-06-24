"""CVS Ingestor.

This script requires that the 'typing, 'os', and 'pandas'
libraries be installed within the Python environment this script
is being run in.
"""

import os
import pandas
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    """A class used if the input file has the extension .csv.

    It realizes the IngestorInterface.

    ...

    Methods:
        can_ingest(path): Returns the boolean value 'True' if the input file
            can be read and 'False' if not.
        parse(path=str): Returns a list of QuoteModels.
    """

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Return a list of QuoteModels containing a quote and the author.

        Arguments:
            path{[str]}: the path where the file to be read is located
        Raises:
            Exception: if the file at the path is not of the correct format
                    or if .csv file at the path cannot be read
        """
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')
        try:
            quotes = []
            path = path.replace('./', '')
            root = os.path.dirname(os.path.dirname(__file__))
            path = os.path.join(root, path).replace('\\', '/')
            input_file = pandas.read_csv(path)
            for i, row in input_file.iterrows():
                new_quote = QuoteModel(row['body'].replace(u"\u2019",
                                                           "'"), row['author'])
                quotes.append(new_quote)
        except Exception as e:
            raise Exception(".csv parsing issue occurred.")
        return quotes
