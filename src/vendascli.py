from typing import (
    Optional,
    Dict,
    Union,
)
import click

from processor import DataProcessor
from views import (
    JsonView,
    TableView,
)

DATA_READER: Optional[DataProcessor] = None

VIEWS:  Dict[str, Union[JsonView, TableView]]= {
    "json": JsonView,
    "text": TableView,
}

@click.command()
@click.argument("file_name", nargs=1)
@click.option("--format", help="Formato do output desejado. Valores suportados são: text | json")
def vendascli(file_name, format):
    if format not in ("text", "json"):
        click.echo(f"Format {format} not supported")
        return

    ViewClass = VIEWS.get(format)
    if DATA_READER is None:
        click.echo("DATA_READER is None. Setting to CSVReader")

    processor = DataProcessor(
        data_reader=DATA_READER
    )
    total_sales = processor.get_net_sale()
    total_value = processor.get_net_value()
    most_frequent = processor.get_most_frequent_product()
    view = ViewClass(
        total_sale_by_prod=processor.get_net_sale(),
        total_salve_value=processor.get_net_value(),
        most_frequent=processor.get_most_frequent_product(),
    )
    to_print = view.parse_output()
    click.echo(to_print)
