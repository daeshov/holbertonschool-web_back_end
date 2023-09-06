#!/usr/bin/env python3
"""Import async_comprehension from the previous file"""
import asyncio
from time import perf_counter
from typing import Generator, List
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ execute async_comprehension four times"""
    start = perf_counter()

    await asyncio.gather(
      async_comprehension(),
      async_comprehension(),
      async_comprehension(),
      async_comprehension())
      """returns value"""
    end = perf_counter()
    total_runtime = end - start
    return total_runtime
