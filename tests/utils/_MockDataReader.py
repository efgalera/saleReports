from typing import (
    Generator,
    List,
    Union,
)

from src.exceptions import InvalidColumnException
from src.interfaces import DataReaderInterface

class MockDataReader(DataReaderInterface):

    def __init__(
        self,
        path_to_data: str,
        ) -> None:
        self.data_path = path_to_data
        self.columns = [
            "produto",
            "quantidade",
            "preço unitário"
        ]
        self.data = [
            ['a', 2, 3],
            ['b', 2, 10],
            ['c', 5, 5],
            ['a', 1, 3],
        ]

    def read(self) -> Generator[List[Union[str, int]]]:
        for row in self.data:
            yield row
    
    def read_all(self) -> List[List[Union[str, int]]]:
        return self.data
    
    def get_columns(self) -> List[str]:
        return self.columns
    
    def get_rows(
        self,
        column: str,
        value: str,
    ) -> List[List[Union[str, int]]]:
        try:
            data_index = self.columns.index(column)

        except ValueError as e:
            # TODO: start adding some logs
            raise InvalidColumnException(f"Failed to find column: {column}")

        res = []
        for row in self.read():
            if not row[data_index] == value:
                continue
            
            res.append(row)

        return res 
