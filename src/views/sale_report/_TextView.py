from typing import List, Tuple

class TextView:
    def __init__(
        self,
        total_sale_by_prod: List[Tuple[str, float]],
        overall_sales: float,
        most_sold_prod: str,
    ) -> None:
        self.total_sale_by_prod = total_sale_by_prod
        self.overall_sales = overall_sales
        self.most_sold_prod = most_sold_prod

    def create(self):
        res = ["This is the Sale Report as text"]
        for prodn, val in self.total_sale_by_prod:
            res.append(f"product {prodn} - sold {val}")

        res.append(f"Overall sales {self.overall_sales}")
        res.append(f"Product with most sales {self.most_sold_prod}")

        return "\n".join(res)
        
