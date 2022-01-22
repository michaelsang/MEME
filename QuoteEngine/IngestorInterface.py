
from abc import ABC, abstractmethod
from typing import List

from .QuoteModel import QuoteModel

class IngestorInterface(ABC):
    """Implement an abstract base class, IngestorInterface."""

    extensions = []

    @classmethod
    def can_ingest(cls,path:str) -> bool:
        """Verify if the path is an injestable format txt,csv,pdf,docx."""
        ext = path.split('.')[-1]
        return ext in cls.extensions

    @classmethod
    @abstractmethod
    def parse(cls, path: str) -> List[QuoteModel]:
        """This is overwritten."""
        pass
#        if not cls.can_ingest(path):
#            raise Exception('Cannot ingest exception')
