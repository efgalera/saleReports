from typing import (
    List,
    Generator,
)

class CSVHandler:
    def __init__(
        self,
        path_to_file: str,
        encoding: str="latin-1",
    ) -> None:
        self.path_to_file = path_to_file
        self.encoding = encoding
        with open(path_to_file, "r", encoding=encoding) as f:
            line = f.readline()
            self.columns = line[:-1].split(",")
        
    def read(self) -> Generator[List[str]]:
        with open(self.path_to_file, "r", encoding=self.encoding) as f:
            _ = f.readline()
            for line in f:
                yield line[:-1].split(",")

    def read_all(self) -> List[str]:
        res = []
        with open(self.path_to_file, "r", encoding=self.encoding) as f:
            _ = f.readline()
            for line in f:
                res.append(line[:-1].split(","))

        return res

    def get_column_index(
        self,
        column_name: str) -> int:
        return self.columns.index(column_name)
    
    def get_distinct_values(self, column: str):
        idx = self.get_column_index(column_name=column)
        res = []
        for line in self.read():
            if line[idx] in res:
                continue

            res.append(line[idx])

        return res