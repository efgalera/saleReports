from typing import List, Tuple

from interfaces import ViewInterface


class TableView(ViewInterface):

    def __init__(
            self,
            total_sale_by_prod: List[Tuple[str, int]],
            total_salve_value: float,
            most_frequent: str):
        super().__init__(
            total_sale_by_prod=total_sale_by_prod,
            total_salve_value=total_salve_value,
            most_frequent=most_frequent
        )

    def parse_output(self):
        prod_table  = "** total vendas por produto **\n"
        prod_table += "      produto | quantidade    \n"
        for row in self.total_sale_by_prod:
            prod_table += f"      {row[0]} | {[row[1]]}\n"
        
        total_value = f"\n\n** total de vendas - valor: {self.total_salve_value}\n"
        most_frequent = f"\n** produto mais vendido: {self.most_frequent}\n"
        return prod_table + total_value + most_frequent

