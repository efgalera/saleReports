import pytest

from src.reports import Report
from src.datahandler import CSVHandler
from src.reports.customexception import InvalidOperationExcetion

@pytest.fixture
def report() -> Report:
    csv_handler = CSVHandler(path_to_file="tests/data/vendas_exemplo - python.csv")
    return Report(data_handler=csv_handler)

def test_report_column_sum(report: Report) -> None:
    val = report.sum_column(column_name="col2")
    assert val == 7.0

def test_report_fail_to_sum(report: Report):
    with pytest.raises(InvalidOperationExcetion):
        val = report.sum_column(column_name="col1")

def test_group_by(report: Report):
    res = report.group_by(column="col1", value="b")
    assert res == [["b","2","99.9"]]

def test_group(report: Report):
    for grp, rows in report.group("col1"):
        if "b" == grp:
            assert rows == [["b","2","99.9"]]