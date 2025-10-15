from click.testing import CliRunner

from src.vendascli import vendascli
import src.vendascli as vds

from .utils import MockDataReader

def test_views():
    runner = CliRunner()
    vds.DATA_READER = MockDataReader(path_to_data="somewhere/to/be")
    runner.invoke(vendascli, ["test.csv", "--format", "text"])
    runner.invoke(vendascli, ["test.csv", "--format", "json"])
    