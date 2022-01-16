"""An ingestor for reading text files."""
import random
import subprocess
from typing import List
from .QuoteModel import QuoteModel
from .IngestorInterface import IngestorInterface


class PdfIngestor(IngestorInterface):
    """Ingestor class makes use of all other classes.

    Each ingestor has a can_ingest function to validate if it can ingest the file."""

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        if not cls.can_ingest(path):
            raise Exception('cannot ingest exception')

        quotes = []
        try:
            tmp = f'./_data/DogQuotes/{random.randint(0, 1000000)}.txt'
            call = subprocess.call(['C:/Users/mkhsa/xpdf-tools-win-4.03/bin64/pdftotext.exe', path, tmp])
            #call = subprocess.call(['pdftotext', path, tmp])  #does not work unless fully specified path

            pdf_file = open(tmp, "r")
            quotes = []

            for line in pdf_file.readlines():
                line = line.strip('\r').strip()
                if len(line) > 0:
                    csv_parse = line.split('-')
                    csv_quote = QuoteModel(csv_parse[0], (csv_parse[1]))
                    quotes.append(csv_quote)
            return quotes


        except Exception as e:
            raise Exception("Text file parsing error occurred.")

    # https://knowledge.udacity.com/questions/572306
    # https://knowledge.udacity.com/questions/633566
    # https://knowledge.udacity.com/questions/606034#632538