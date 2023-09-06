import asyncio
import random

async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)  # Generate a random float between 0 and max_delay
    await asyncio.sleep(delay)  # Asynchronously wait for the generated delay
    return delay
