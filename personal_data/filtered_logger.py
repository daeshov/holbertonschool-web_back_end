#!/usr/bin/env python3
"""a function called filter_datum
that returns the log message obfuscated
"""
import logging
import re
import os
import mysql.connector
from typing import List
PII_FIELDS = ('name', 'email', 'phone', 'ssn', 'password')


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
        """constuctor"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields_redacted = fields

    def format(self, record: logging.LogRecord) -> str:
        """ filter values in incoming log
        records using filter_datum"""
        message = super().format(record)
        for field in self.fields_redacted:
            message = filter_datum(
                [field], self.REDACTION, message, self.SEPARATOR)
        return message


def get_logger() -> logging.Logger:
    """function that takes no arguments and
    returns a logging.Logger object"""
    logger = logging.getLogger("user_data")
    logger.setLevel(logging.INFO)
    logger.propagate = False
    handler = logging.StreamHandler()
    formatter = RedactingFormatter(List(PII_FIELDS))
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger


def get_db() -> mysql.connector.connection.MySQLConnection:
    """Returns: mysql.connector"""
    return mysql.connection.connect(
        host=os.getenv('PERSONAL_DATA_DB_HOST, localhost'),
        database=os.getenv('PERSONAL_DATA_DB_USERNAME'),
        user=os.getenv('PERSONAL_DATA_DB_USERNAME', 'root'),
        password=os.getenv('PERSONAL_DATA_DB_USERNAME', '')
    )
