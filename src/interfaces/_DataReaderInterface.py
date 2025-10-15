from typing import (
    List,
    Union,
)
from abc import (
    ABC,
    abstractmethod,
    )

class DataReaderInterface(ABC):
    RowType = List[Union[str, int, float]]

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
    ) -> List[RowType]:
        raise NotImplementedError()