class QuoteModel:
    author = None
    line = None

    def __init__(self, body, author):
        self.body = body
        self.author = author
