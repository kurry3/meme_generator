import os
import pandas
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class CSVIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
