import pytest

from src.reports import Report
from src.datahandler import CSVHandler
from src.reports.customexception import InvalidColumnName

@pytest.fixture
def report() -> Report:
    csv_handler = CSVHandler(path_to_file="tests/data/vendas_exemplo - python.csv")
    return Report(data_handler=csv_handler)

def test_report_column_sum(report: Report) -> None:
    val = report.all_values(column_name="col2")
    assert val == ['3', '2', '1', '1']

def test_report_fail_to_sum(report: Report):
    with pytest.raises(InvalidColumnName):
        val = report.all_values(column_name="col9")

def test_group_by(report: Report):
    res = report.group_by(column="col1", value="b")
    assert res == [{"col1": "b","col2": "2","col3": "99.9"}]

def test_group(report: Report):
    for grp, rows in report.group("col1"):
        if "b" == grp:
            assert rows == [{"col1": "b","col2": "2","col3": "99.9"}]