#!/usr/bin/env python3

"""type-annotated function make_multiplier that takes
a float multiplier as argument"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def multiplier_function(x: float) -> float:

        return (x * multiplier)
        """returns a function that multiplies a float by multiplier"""
    return multiplier_function
