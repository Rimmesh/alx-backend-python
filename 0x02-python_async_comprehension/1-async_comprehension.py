#!/usr/bin/env python3
import asyncio
from typing import List
from 0_async_generator import async_generator

async def async_comprehension() -> List[float]:
    """Collect 10 random numbers using an async comprehensing over async_generator, then return the 10 random numbers."""
    return [number async for number in async_generator()]
