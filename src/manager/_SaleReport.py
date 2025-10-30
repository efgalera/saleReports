from src.reports import Report
from src.datahandler import CSVHandler
from src.views.utils import get_sale_report_view


class SaleReport:
    def __init__(
        self,
        data_file_name: str,
        view_name: str,
    ) -> None:
        csv_handler = CSVHandler(path_to_file=data_file_name)
        report = Report(data_handler=csv_handler)
        self.report = report
        self.prod_column = "produto"
        self.view = get_sale_report_view(name=view_name)

    def make_report(self):
        total_sale = self.report.sum_column(column_name="preco_unitario")
        # total_by_prod = self._get_total_sale_by_product()