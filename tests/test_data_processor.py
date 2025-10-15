import pytest

from src.processor import DataProcessor

from .utils import MockDataReader


@pytest.fixture
def processor():
    mock_reader = MockDataReader(
        path_to_data="path/to/somewhere"
    )
    return DataProcessor(
        data_reader=mock_reader
    )

def test_sale_by_product(processor: DataProcessor):
    total_sale_a = processor.get_total_sale_by_product(product="a")
    total_sale_b = processor.get_total_sale_by_product(product="b")
    total_sale_c = processor.get_total_sale_by_product(product="c")
    assert [total_sale_a, total_sale_b, total_sale_c] == [3, 2, 5]

def test_sale_value(processor: DataProcessor):
    net_value = processor.get_net_value()
    assert net_value == 21

def test_most_frequent_product(processor: DataProcessor):
    prod = processor.get_most_frequent_product()
    assert prod == "c"


def test_net_sale(processor: DataProcessor):
    net_sale = processor.get_net_sale()
    assert net_sale == [("a", 3), ("b", 2), ("c", 5)]
