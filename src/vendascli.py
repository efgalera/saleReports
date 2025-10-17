import os
import click

from processor import DataProcessor
from exceptions import InvalidArgummentException
from views import (
    JsonView,
    TableView,
)

from datahandler import CSVHandler

VIEWS = {
    "json": JsonView,
    "text": TableView,
}

@click.command()
@click.argument("file_name", nargs=1)
@click.option("--format", required=True, help="Formato do output desejado. Valores suportados são: text | json")
@click.option("--start", required=False, help="Data de inicio para filtrar: aceitos x > start")
@click.option("--end", required=False, help="Data final para filtrar: aceitos x < end")
def vendascli(file_name, format, start, end):
    if format not in VIEWS.keys():
        raise InvalidArgummentException(f"Format {format} not supported")
    
    if not os.path.exists(file_name):
        raise FileNotFoundError(f"Failed to find {file_name}")

    if start or end:
        click.echo("Filtro por datas será implementado na próxima versão")

    ViewClass = VIEWS[format]
    csv_handler = CSVHandler(path_to_data=file_name)

    processor = DataProcessor(
        data_reader=csv_handler
    )
    view = ViewClass(
        total_sale_by_prod=processor.get_net_sale(),
        total_salve_value=processor.get_net_value(),
        most_frequent=processor.get_most_frequent_product(),
    )
    to_print = view.parse_output()
    click.echo(to_print)
