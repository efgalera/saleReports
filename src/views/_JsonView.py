from typing import List, Union

from interfaces import ViewInterface


class JsonView(ViewInterface):

    def __init__(
            self,
            total_sale_by_prod: List[str | int],
            total_salve_value: float,
            most_frequent: str):
        super().__init__(
            total_sale_by_prod=total_sale_by_prod,
            total_salve_value=total_salve_value,
            most_frequent=most_frequent
        )

    def parse_output(self):
        data = {
            "total_vendas_prod": [
                {k: v} for k, v in self.total_sale_by_prod
            ],
            "total_valor_vendas": self.total_salve_value,
            "mais_vendido": self.most_frequent
        }
        return data
