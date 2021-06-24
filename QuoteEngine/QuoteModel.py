"""QuoteModel.

No necessary library installations to run this file.
"""


class QuoteModel:
    """A class to encapsulate the body and author of input quotes.

    ...

    Attributes:
        author: str
            str containing the author of the quote
        body: str
            str containing the body of the quote
    """

    author = None
    body = None

    def __init__(self, body, author):
        """Instantiate class attributes.

        Parameters:
            author: str
                str containing the author of the quote
            body: str
                str containing the body of the quote
        """
        self.body = body
        self.author = author
