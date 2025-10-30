from typing import (
    Dict,
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
        
    def _cast_line(self, line: str) -> Dict[str, str]:
        return {col: val for col, val in  zip(self.columns,line[:-1].split(","))}

    def read(self) -> Generator[Dict[str, str]]:
        with open(self.path_to_file, "r", encoding=self.encoding) as f:
            _ = f.readline()
            for line in f:
                yield self._cast_line(line=line)

    def read_all(self) -> List[Dict[str, str]]:
        res = []
        with open(self.path_to_file, "r", encoding=self.encoding) as f:
            _ = f.readline()
            for line in f:
                res.append(self._cast_line(line=line))

        return res

    def get_distinct_values(self, column: str):
        res = []
        for line in self.read():
            if line[column] in res:
                continue

            res.append(line[column])

        return res