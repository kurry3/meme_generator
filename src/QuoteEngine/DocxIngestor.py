from typing import List
import docx
import os

from .IngestorInterface import IngestorInterface
from .QuoteModel import QuoteModel


class DocxIngestor(IngestorInterface):
    allowed_extensions = ['docx']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
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
