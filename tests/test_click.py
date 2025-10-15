import pytest
from click.testing import CliRunner

from src.vendascli import vendascli
from src.exceptions import InvalidArgummentException


def test_views():
    runner = CliRunner()
    runner.invoke(vendascli, ["vendas_exemplo - python.csv", "--format", "text"])
    runner.invoke(vendascli, ["vendas_exemplo - python.csv", "--format", "json"])

# TODO: CliRunner is suppersing exceptions and making pytest.raises fail.
def test_handle_exception():
    runner = CliRunner()
    runner.invoke(vendascli, ["vendas_exemplo - python.csv", "--format", "not suported"])

def test_file_not_exists():
    runner = CliRunner()
    runner.invoke(vendascli, ["i_dont_exist.csv", "--format", "text"])