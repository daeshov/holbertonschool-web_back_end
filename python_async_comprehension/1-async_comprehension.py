#!/usr/bin/env python3
"""takes no arguments"""
import asyncio
import random
from typing import Generator, List 
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """"""
    random_numbers = [random_numbers async for i in async_generator()]
    return random_numbers
