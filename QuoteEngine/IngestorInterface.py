
from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel

ingestors = {
    "CSV": ".csv",
    "DOCX": ".docx",
    "PDF": ".pdf",
    "TEXT": ".txt",
}

class IngestorInterface(ABC):
    """Implement an abstract base class, IngestorInterface.
    The IngestorInterface defines the common functionalities (methods) that need to be implemented by the Interface classes.
    This class defines two methods with the following class method signatures.
    https://knowledge.udacity.com/questions/439686
    def can_ingest(clr, path) -> bool:
    def parse(clr, path: str) -> List[QuoteModel]:
    """

    @classmethod
    def can_ingest(cls,path:str) -> bool:
        """can_ingest class method is supposed to receive a path and determine if the path is an injestable format (txt,csv,pdf,docx)."""
        return path.split('.')[-1] in ['txt','csv','pdf','docx']



    @classmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """Select the appropriate helper for a given file based on filetype."""
        for ingestor in cls.ingestors:
            if ingestor.can_ingest(path):
                return ingestor.parse(path)


