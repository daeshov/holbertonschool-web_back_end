#!/usr/bin/env python3
import asyncio
import random
import time
from typing import List


async def wait_random(max_delay: int = 10) -> float:
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay


async def wait_n(n: int, max_delay: int) -> List[float]:

    delays = await asyncio.gather(*(wait_random(max_delay) for _ in range(n)))
    return sorted(delays)

async def measure_time(n: int, max_delay: int) -> List[float]:

    start = time.time()
    asyncio.run(wait_n(n, max_delay))
    end = time.time()
    total_time end - start
    return total_time / n
