#!/usr/bin/env python3
"""Filtered logger."""
import re
from typing import List

def filter_datum() -> str:
    """Filter datum."""
    pass


if __name__ == "__main__":
    fields = ["password", "date_of_birth"]
    messages = [
            "name=egg;email=eggmin@eggsample.com;password=eggcellent;date_of_birth=12/12/1986;",
            "name=bob;email=bob@dylan.com;password=bobbycool;date_of_birth=03/04/1993;"
            ]

    for message in messages:
        print(filter_datum(fields, 'xxx', message, ';'))
