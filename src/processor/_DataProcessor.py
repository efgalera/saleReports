from typing import List, Union

from interfaces import DataReaderInterface

class DataProcessor:
    def __init__(
        self,
        data_reader: DataReaderInterface
    ) -> None:
        self.data_reader = data_reader
