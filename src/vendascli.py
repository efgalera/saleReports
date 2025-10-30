import os
import click

from manager import SaleReport


@click.command()
@click.argument("file_name", nargs=1)
@click.option("--format", required=True, help="Formato do output desejado. Valores suportados são: text | json")
@click.option("--start", required=False, help="Data de inicio para filtrar: aceitos x > start")
@click.option("--end", required=False, help="Data final para filtrar: aceitos x < end")
def vendascli(file_name, format, start, end):
    sale_report = SaleReport(
        data_file_name=file_name,
        view_name=format,
    )
    click.echo(sale_report.make_report())

if __name__ == "__main__":
    sale_report = SaleReport(
        data_file_name="vendas_exemplo - python.csv",
        view_name="text",
    )
    click.echo(sale_report.make_report())