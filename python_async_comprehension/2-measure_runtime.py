#!/usr/bin/env python3
"""takes no arguments"""
import asyncio
import random
from time import perf_counter
from typing import Generator, List 
async_generator = __import__('1-async_comprehension').async_generator


async def measure_runtime () -> List float:
    """"""
    start = perf_counter()

    await asyncio.gather(
    async_comprehension(),
    async_comprehension(),
    async_comprehension(),
    async_comprehension())

    end = perf_counter()
    total_runtime = end - start
    return total_runtime
