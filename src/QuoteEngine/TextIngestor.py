import os
from typing import List
from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class TextIngestor(IngestorInterface):
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
