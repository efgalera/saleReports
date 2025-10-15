from typing import (
    List,
    Union,
)
from abc import (
    ABC,
    abstractmethod,
    )

class DataReaderInterface(ABC):

    @abstractmethod
    def read(self):
        raise NotImplementedError()
    
    @abstractmethod
    def read_all(self):
        raise NotImplementedError()
    
    @abstractmethod
    def get_columns(self):
        raise NotImplementedError()
    
    @abstractmethod
    def get_rows(
        self,
        column: str,
        value: str,
    ) -> List[List[Union[str, int]]]:
        raise NotImplementedError()