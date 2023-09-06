#!/usr/bin/env python3
"""Task 4"""
import random
import asyncio
from typing import List
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Return a list of delays"""
    list_delays = []
    for i in range(n):
        list_delays.append(await task_wait_random(max_delay))
    return sorted(list_delays)
