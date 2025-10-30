from typing import (
    List,
    Tuple,
    Any,
    Generator,
    Dict,
)

from datahandler import CSVHandler
from .customexception import InvalidColumnName

class Report:
    def __init__(
        self,
        data_handler: CSVHandler,
    ) -> None:
        self.data_handler = data_handler

    def all_values(self, column_name: str) -> List[str]:
        res = []
        for line in self.data_handler.read():
            try:
                res.append(line[column_name])

            except KeyError:
                raise InvalidColumnName(f"Failed to get column {column_name} in data set")
            
        return res
    
    def group_by(
        self,
        column: str,
        value:str
    ) -> List[Dict[str, str]]:
        res = []
        for line in self.data_handler.read():
            if line[column] == value:
                res.append(line)
        
        return res
    
    def group(
        self,
        column: str,
    ) -> Generator[Tuple[str, List[Any]]]:
        for val in self.data_handler.get_distinct_values(column=column):
            yield (val, self.group_by(column=column, value=val))
