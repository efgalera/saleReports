from reports import Report
from datahandler import CSVHandler
from views.utils import get_sale_report_view


class SaleReport:
    def __init__(
        self,
        data_file_name: str,
        view_name: str,
    ) -> None:
        csv_handler = CSVHandler(path_to_file=data_file_name)
        report = Report(data_handler=csv_handler)
        self.report = report
        self.view = get_sale_report_view(name=view_name)

    def make_report(self):
        unit_price_list = self.report.all_values(column_name="preco_unitario")
        quantity_list = self.report.all_values(column_name="quantidade")
        absolute_total = 0.0
        for qty, uprice in zip(quantity_list, unit_price_list):
            absolute_total += float(qty)*float(uprice)

        total_by_prod = {}
        most_frequent = {}
        for grp, rows in self.report.group(column="produto"):
            aux = 0.0
            aux2 = 0.0
            for row in rows:
                qty = float(row["quantidade"])
                price = float(row["preco_unitario"])
                aux += qty * price
                aux2 += qty
            total_by_prod.update({grp: aux})
            most_frequent.update({grp: aux2})

        view = self.view(
            total_sale_by_prod=total_by_prod,
            overall_sales=absolute_total,
            most_sold_prod=most_frequent,
        )
        return view.create()
