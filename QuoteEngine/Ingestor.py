from .IngestorInterface import IngestorInterface

from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .CsvIngestor import CsvIngestor
from .PdfIngestor import PdfIngestor

from .QuoteModel import QuoteModel
from typing import List


class Ingestor(IngestorInterface):
    """A final Ingestor class should realize the IngestorInterface
    abstract base class and encapsulate your helper classes.

    It should implement logic to choose the appropriate helper ingestor
    type based on filetype.
    """

    ingestors = [TextIngestor, DocxIngestor, CsvIngestor, PdfIngestor]

    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select the appropriate helper for a given file based on filetype."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)
