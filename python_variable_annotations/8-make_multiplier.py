#!/usr/bin/env python3
"""type-annotated function make_multiplier"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """take a float multiplier as argument"""
    def multiplier_function(x: float) -> float:

        return (x * multiplier)
        """returns a function that multiplies a float by multiplier"""
    return multiplier_function
