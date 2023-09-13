#!/usr/bin/env python3
""" task 0
a function named index_range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ a function named index_range that
    takes two integer arguments page and page_size """
    return ((page - 1) * page_size, page * page_size)
