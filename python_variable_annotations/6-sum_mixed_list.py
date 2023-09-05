#!/usr/bin/env python3

"""type-annotated function sum_mixed_list which takes 
a list mxd_lst of integers and floats and returns their sum as a float"""
from typing import List

def sum_mixed_list(mxd_lst: List[int, float]) -> float:

  return sum(mxd_lst)
