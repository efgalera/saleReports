import pytest

from src.datahandler import CSVHandler

@pytest.fixture
def handler() -> CSVHandler:
    return CSVHandler(path_to_file="tests/data/vendas_exemplo - python.csv")

def test_columns(handler: CSVHandler):
    assert handler.columns == ["col1","col2","col3"]

def test_read_all(handler: CSVHandler):
    all_lines = handler.read_all()
    assert len(all_lines) == 4
    assert all_lines[0] == ["a","3","49.9"]


def test_read(handler: CSVHandler):
    res = []
    for line in handler.read():
        colum_index = handler.get_column_index(handler.columns[0])
        res.append(line[colum_index])

    assert res == ["a", "b", "a", "c"]

def test_get_distinct(handler: CSVHandler):
    assert handler.get_distinct_values(column="col1") == ["a", "b", "c"]