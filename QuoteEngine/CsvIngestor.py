"""An ingestor for reading text files."""
from typing import List
import pandas as pd
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class CsvIngestor(IngestorInterface):
    """Ingestor class makes use of all other classes.

    Each ingestor has a can_ingest function to validate if it can ingest the file."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        try:
            csv = pd.read_csv(path)

            for index, row in csv.iterrows():
                csv_quote = QuoteModel(row['body'].strip(), row['author'].strip())
                quotes.append(csv_quote)
            return quotes


        except Exception as e:
            raise Exception("Text file parsing error occurred.")
