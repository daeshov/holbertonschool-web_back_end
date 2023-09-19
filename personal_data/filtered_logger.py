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
        pattern = re.compile(f"({field}=.+?{separator})")
        message = re.sub(pattern, f"{field}={redaction}{separator}", message)
    return message


class RedactingFormatter(logging.Formatter):
    """ Redacting Formatter class
        """

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields_redacted = fields

    def format(self, record: logging.LogRecord) -> str:
        message = super().format(record)
        for field in self.fields_redacted
        message = filter_datum(
            [field],
            self.REDACTION,
            message,
            self.SEPARATOR)
        return message
