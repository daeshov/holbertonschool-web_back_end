#!/usr/bin/env python3
"""
hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class for paginating a database of popular baby names."""

    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """Initialize the Server instance."""
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Get the cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Get the dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Return a dictionary with indexed pagination details."""
        self.indexed_dataset()
        _list = []
        for datas in self.__indexed_dataset:
            if datas >= index and datas <= (page_size + index):
                _list.append(self.__indexed_dataset[datas])
        _dict = {
            "index": index,
            "data": _list,
            "page_size": page_size,
            "next_index": index + page_size
        }
        return _dict
