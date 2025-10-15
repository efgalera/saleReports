import pytest

from src.interfaces import DataReaderInterface
from src.exceptions import InvalidColumnException

from .utils import MockDataReader

@pytest.fixture
def mockreader() -> DataReaderInterface:
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