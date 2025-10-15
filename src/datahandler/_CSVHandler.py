from typing import (
    Generator,
    List,
    Union,
)

from interfaces import (
    DataReaderInterface,
    )
from exceptions import InvalidColumnException


RowType = DataReaderInterface.RowType

class CSVHandler(DataReaderInterface):

    def __init__(
        self,
        path_to_data: str
    ) -> None:
        super().__init__()
        self.path_to_data: str = path_to_data
        self._type_mask: List[type] = [
            str,
            int,
            float
        ]
        with open(path_to_data, "r", encoding="latin-1") as f:
            line = f.readline()
            self.columns = line[:-1].split(",") 

    def _cast_line_to_data(
        self,
        line: str
    ) -> RowType:
        splited = line.split(",")
        return [tp(val) for tp, val in zip(self._type_mask, splited)]
            
    def read(self) -> Generator[RowType]:
        column_name = True
        with open(self.path_to_data, "r", encoding="latin-1") as f:
            for line in f:
                if column_name:
                    column_name = False
                    continue
                yield self._cast_line_to_data(line)

    def read_all(self) -> List[RowType]:
        res = []
        column_name = True
        with open(self.path_to_data, "r", encoding="latin-1") as f:
            for line in f:
                if column_name:
                    column_name = False
                    continue

                res.append(self._cast_line_to_data(line=line))

        return res

    def get_columns(self) -> List[str]:
        return self.columns

    def get_rows(
        self,
        column: str,
        value: str,
    ) -> List[RowType]:
        
        try:
            data_index: int = self.columns.index(column)

        except ValueError as e:
            # TODO: start adding some logs
            raise InvalidColumnException(f"Failed to find column: {column}")

        res: List[RowType] = []
        for row in self.read():
            if not row[data_index] == value:
                continue
            
            res.append(row)

        return res 