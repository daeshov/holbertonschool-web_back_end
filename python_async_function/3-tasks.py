#!/usr/bin/env python3
"""task 3"""

import asyncio
import random
import time
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    """return asyncio.Tasks"""

    Tasks = asyncio.create_task(wait_random(max_delay))
    return Tasks
