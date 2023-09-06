#!/usr/bin/env python3

"""type-annotated function to_kv that takes a string k
and an int OR float v as arguments and returns a tuple. The first element of the tuple is the string k. 
The second element is the square of the int/float v and should be annotated as a float"""
from typing import Callable

def make_multiplier(multiplier: float) ->  Callable[[float], float]:

  def multiplier_function(x: float) -> float:
      return x *multiplier
return multiplier_function
