from typing import List

from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class TextIngestor(IngestorInterface):
    """Ingestor class makes use of all other classes.

    Ingestor class inherits the IngestorInterface.
    Each ingestor has a can_ingest function to validate
    if it can ingest the file."""

    extensions = ['txt']

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        try:
            text_file = open(path, 'r', encoding="utf-8")
            for lines in text_file.readlines():
                line = lines.strip('')
                if len(line) > 0:
                    text_parse = lines.split('-')
                    text_quote = QuoteModel(str(text_parse[0].strip()),
                                           str(text_parse[1].strip()))
                    quotes.append(text_quote)
            text_file.close()
            return quotes

        except Exception as e:
            raise Exception("Text file parsing error occurred.")

