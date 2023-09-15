#!/usr/bin/env python3
"""a function called filter_datum
that returns the log message obfuscated
"""
import logging
import re


def filter_datum(fields, redaction, message, separtor):
    regex = rf'({separtor.join})\s*:\s*\S+'
    return re.sub(regex,f'\\1: {redaction}', message)
