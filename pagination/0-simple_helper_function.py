#!/usr/bin/env python3 
""" task 0
a function named index_range"""

def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """ a function named index_range"""
    return ((page - 1)* page_size, page * page_size)
