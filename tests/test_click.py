from click.testing import CliRunner

from src.vendascli import vendascli
import src.vendascli as vds

from src.datahandler import CSVHandler

def test_views():
    runner = CliRunner()
    runner.invoke(vendascli, ["vendas_exemplo - python.csv", "--format", "text"])
    runner.invoke(vendascli, ["vendas_exemplo - python.csv", "--format", "json"])
    