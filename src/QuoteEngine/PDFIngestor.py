import os
import subprocess
import random
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class PDFIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
