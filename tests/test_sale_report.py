import pytest

from src.manager import SaleReport

@pytest.fixture
def report() -> SaleReport:
    sale_report = SaleReport(
        data_file_name="tests/data/test_sample_data.csv",
        view_name="text"
    )
    return sale_report


def test_sale_report(report: SaleReport):
    report.make_report()
    pass