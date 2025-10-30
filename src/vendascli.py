import os
import click


@click.command()
@click.argument("file_name", nargs=1)
@click.option("--format", required=True, help="Formato do output desejado. Valores suportados são: text | json")
@click.option("--start", required=False, help="Data de inicio para filtrar: aceitos x > start")
@click.option("--end", required=False, help="Data final para filtrar: aceitos x < end")
def vendascli(file_name, format, start, end):
    click.echo("Under new management")