#!/usr/bin/env python3
"""takes no arguments"""
from async_generator import async_generator
import asyncio
import random
from typing import Generator, List 


async def async_comprehension() -> List[float]:
    """"""
    random_numbers = [random_numbers async for i in async_generator()]
    return random_numbers
