#!/usr/bin/env python3
""" task 0
a function named index_range"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ a function named index_range that
    takes two integer arguments page and page_size """
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Implement a method named get_page that takes two integer
        arguments page with default value 1 and page_size 
        with default value 10.
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        dataset = self.dataset()
        total_rows = len(dataset)
        start_index, end_index = index_range(page, page_size)

        if start_index >= total_rows:
            return []
        end_index = min(end_index, total_rows - 1)

        result = dataset[start_index:end_index + 1]

        assert len(result) == end_index - start_index + 1, "Returned list has an incorrect length"
        
        return result
