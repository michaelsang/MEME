
from .IngestorInterface import IngestorInterface

from .TextIngestor import TextIngestor
from .DocxIngestor import DocxIngestor
from .CsvIngestor import CsvIngestor
from .PdfIngestor import PdfIngestor

from .QuoteModel import QuoteModel
from typing import List

class Ingestor(IngestorInterface):
    """A final Ingestor class should realize the IngestorInterface abstract base class and encapsulate your helper classes.

    It should implement logic to choose the appropriate helper ingestor type based on filetype.
    """

    ingestors = [TextIngestor, DocxIngestor, CsvIngestor, PdfIngestor]
    # https://knowledge.udacity.com/questions/439686

    """
    The IngestorInterface defines the common functionalities (methods) that need to be implemented by the Interface classes. The purpose of the Interface is to define the common methods without the logic i.e. they don't have body of the function.

For example: There are two Ingestor classes CSVIngestor and PDFIngestor. There's a IngestorInterface that contains the method "Decode". So, both ingestors will decode a file but the logic for decode will be different for both the classes. So the common functionality (Decode Function) is defined in the IngestorInterface without body. The Ingestor classes implement the Interface and override the "Decode" Method, thereby providing functionality based on class's requirements.

This is simply an architectural concept. You can learn more about the ‌Python Interface‌

Thanks!
    
    """
    #https://knowledge.udacity.com/questions/559464
    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select the appropriate helper for a given file based on filetype."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)


