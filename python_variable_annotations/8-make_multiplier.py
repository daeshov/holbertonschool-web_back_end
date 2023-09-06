#!/usr/bin/env python3

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """type-annotated function make_multiplier that takes
    a float multiplier as argument"""
    def multiplier_function(x: float) -> float:

        return (x * multiplier)
        """returns a function that multiplies a float by multiplier"""
    return multiplier_function
