#!/usr/bin/env python3
"""task 1: async """


import asyncio
import random
from typing import Generator, List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """random 10"""
    random_numbers = [i async for i in async_generator()]
    return random_numbers
