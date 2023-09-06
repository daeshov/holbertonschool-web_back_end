#!/usr/bin/env python3
"""takes no arguments"""
import asyncio
from time import perf_counter
from typing import Generator, List 
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime():
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
