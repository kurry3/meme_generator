"""IngestorInterface.

This script requires that the 'typing', 'abc' and 'os'
libraries be installed within the Python environment this script
is being run in.
"""

import os
from abc import ABC, abstractmethod
from typing import List
from .QuoteModel import QuoteModel

extensions = ['.txt', '.csv', '.pdf', '.docx']


class IngestorInterface(ABC):
    """An abstract base class.

    ...

    Methods:
        can_ingest(path): Returns the boolean value 'True' if the input file
            can be read and 'False' if not.
        parse(path=str): inheriting classes will redefine this empty function
    """

    @classmethod
    def can_ingest(cls, path) -> bool:
        """Return boolean 'True' if the input file can be read else 'False'.

        Arguments:
            path{[str]}: the path where the file to be read is located
        """
        filename, file_extension = os.path.splitext(path)
        if file_extension in extensions:
            return True
        else:
            return False

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Empty function for later definition by inheriting classes."""
        pass
