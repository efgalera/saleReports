from typing import List, Union

class ViewInterface:

    def __init__(
        self,
        total_sale_by_prod: List[Union[str, int]],
        total_salve_value: float,
        most_frequent: str,
    ):
        self.total_sale_by_prod = total_sale_by_prod
        self.total_salve_value = total_salve_value
        self.most_frequent = most_frequent

    def parse_output(fields: List[str], values: List[str]) -> None:
        raise NotImplementedError
