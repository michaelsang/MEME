class QuoteModel():
    """QuoteModel class to encapsulate the body and author."""

    def __init__(self, body:str, author:str):
        self.body = body
        self.author = author


    def __str__(self):
        """Return return a human-readable string representation."""
        return f"{self.body} - {self.author}."


    def __repr__(self):
        """Return a computer-readable string representation of this object."""
        """ return ”body text” - author """
        return f'\"{self.body}\" - {self.author}'

