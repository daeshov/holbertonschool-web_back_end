#!/usr/bin/env python3
"""a function called filter_datum
that returns the log message obfuscated
"""
import logging
import re
from typing import List


def filter_datum(fields: List[str], redaction: str, message: str,
                 separator: str) -> str:
    """Returns: log message obfuscated"""
    for field in fields:
        message = re.sub(f"{field}=(.*?){separator}",
                         f"{field}={redaction}{separator}", message)
        return message
