from typing import (
    Dict,
    Tuple,
    List,
)

from interfaces import DataReaderInterface

class DataProcessor:
    def __init__(
        self,
        data_reader: DataReaderInterface
    ) -> None:
        self.data_reader = data_reader

    def _net_sale(self):
        grouping = {}
        for row in self.data_reader.read():
            if row[0] not in grouping:
                grouping.update({row[0]: row[1]})

            else:
                grouping[row[0]] += row[1]

        return grouping

    def get_total_sale_by_product(
        self,
        product: str,
    ) -> int:
        res = 0
        # TODO: the processor should not  know names or index of the dataset
        for row in self.data_reader.get_rows(
            column="produto",
            value=product,
            ):
            res += row[1]

        return res

    def get_net_value(self) -> int:
        res = 0
        for row in self.data_reader.read():
            res += row[2]

        return res

    def get_most_frequent_product(self) -> str:
        grouping = self._net_sale()
        sorted_prods = sorted([(x, y) for x, y in grouping.items()], key=lambda z: z[1])
        return sorted_prods[-1][0]
    
    def get_net_sale(self) -> List[Tuple[str, int]]:
        grouping = self._net_sale()
        return [(x, y) for x, y in grouping.items()]
