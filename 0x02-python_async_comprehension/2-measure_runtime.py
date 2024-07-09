#!/usr/bin/env python3
import asyncio
import time
from typing import List
from 1_async_comprehension import async_comprehension

async def measure_runtime() -> float:
    """Execute async_comprehension four times in parallel using asyncio.gather and measure the total runtime."""
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
