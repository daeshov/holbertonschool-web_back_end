#!/usr/bin/env python3
"""takes no arguments"""
from async_generator import async_generator
import asyncio
import random
from typing import Generator


async def async_comprehension():
    """"""
    random_numbers = [i async for i in async_generator()]
    return random_numbers
