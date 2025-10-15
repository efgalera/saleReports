from typing import List, Generator, Union
import pytest

from src.interfaces import DataReaderInterface
from src.processor import DataProcessor
from src.exceptions import InvalidColumnException

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

@pytest.fixture
def mockreader() -> DataProcessor:
    return MockDataReader(
        path_to_data="path/to/somewhere"
    )

def test_read_csv_columns(mockreader: DataReaderInterface):
    columns = mockreader.get_columns()
    assert columns == [
            "produto",
            "quantidade",
            "preço unitário"
        ]

def test_get_rows(mockreader: DataReaderInterface):
    rows = mockreader.read_all()
    assert rows[0] == ['a', 2, 3]
    assert rows[-1] == ['a', 1, 3]

def test_get_row_by_column_value(mockreader: DataReaderInterface):
    rows = mockreader.get_rows(
        column="produto",
        value="a"
    )
    assert rows == [['a', 2, 3], ['a', 1, 3]]


def test_fail_to_get_row_non_existing_column(mockreader: DataReaderInterface):
    with pytest.raises(InvalidColumnException):
        rows = mockreader.get_rows(
            column="I dont exist",
            value="metaphorical"
        )