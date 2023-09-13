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
        assert isinstance(page) == int and page >= 1
        assert isinstance(page_size) == int and page_size >= 1
        pagination = index_range(page, page_size)
        self.dataset()
        return self.__dataset[pagination[0]:pagination[1]]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Return a dictionary with pagination details."""
        self.dataset()
        total_pages = len(self.dataset())
        data = self.get_page(page, page_size)
        next_page = page + 1 if page + 1 <= total_pages else None
        prev_page = page - 1 if page - 1 >= 1 else None
        return {
            "page_size": page_size,
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }
