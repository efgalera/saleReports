import pytest

from src.processor import DataProcessor
from src.views import (
    JsonView,
    TableView
)

from .utils import MockDataReader

@pytest.fixture
def processor() -> DataProcessor:
    mock_data = MockDataReader("path/to/data")
    return DataProcessor(data_reader=mock_data)


def test_table_view(processor: DataProcessor) -> None:
    view = TableView(
        total_sale_by_prod=processor.get_net_sale(),
        total_salve_value=processor.get_net_value(),
        most_frequent=processor.get_most_frequent_product()
    )
    to_print = view.parse_output()
    assert to_print == "** total vendas por produto **\n      produto | quantidade    \n      a | [3]\n      b | [2]\n      c | [5]\n\n\n** total de vendas - valor: 21\n\n** produto mais vendido: c\n"

def test_json_view(processor: DataProcessor) -> None:
    view = JsonView(
        total_sale_by_prod=processor.get_net_sale(),
        total_salve_value=processor.get_net_value(),
        most_frequent=processor.get_most_frequent_product()
    )
    to_print = view.parse_output()
    assert to_print.get("total_vendas_prod") == [{'a': 3}, {'b': 2}, {'c': 5}]
    assert to_print.get("total_valor_vendas") == 21
