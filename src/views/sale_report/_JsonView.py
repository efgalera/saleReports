from typing import List, Tuple, Dict

class JsonView:
    def __init__(
        self,
        total_sale_by_prod: Dict[str, float],
        overall_sales: float,
        most_sold_prod: str,
    ) -> None:
        self.total_sale_by_prod = total_sale_by_prod
        self.overall_sales = overall_sales
        self.most_sold_prod = most_sold_prod

    def create(self):
        return {
            "total_sales_by_product": self.total_sale_by_prod,
            "overall_sales": self.overall_sales,
            "most_sold_product": self.most_sold_prod,
            }