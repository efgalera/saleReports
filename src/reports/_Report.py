from typing import List, Tuple, Any, Generator

from src.datahandler import CSVHandler
from .customexception import InvalidOperationExcetion, InvalidColumnName

class Report:
    def __init__(
        self,
        data_handler: CSVHandler,
    ) -> None:
        self.data_handler = data_handler

    def sum_column(self, column_name: str) -> float:
        data_index = self.data_handler.get_column_index(column_name=column_name)
        res = 0.0
        for line in self.data_handler.read():
            try:
                res += float(line[data_index])

            except ValueError:
                raise InvalidOperationExcetion(f"Failed to convert {column_name} to number")
            
        return res
    
    def group_by(
        self,
        column: str,
        value:str
    ) -> List[List[str]]:
        index = self.data_handler.get_column_index(column_name=column)
        res = []
        for line in self.data_handler.read():
            if line[index] == value:
                res.append(line)
        
        return res
    
    def group(
        self,
        column: str,
    ) -> Generator[Tuple[str, List[Any]]]:
        for val in self.data_handler.get_distinct_values(column=column):
            yield (val, self.group_by(column=column, value=val))

    def colum_idx(
        self,
        column: str
    ) -> int:
        try:
            return self.data_handler.get_column_index(column_name=column)
        except ValueError:
            raise InvalidColumnName(f"Failed to get index for column {column}")

