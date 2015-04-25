#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Task 02 module"""


import datetime


class InvalidAgeError(Exception):
    """Impossible age class."""
    pass


def get_age(birthyear):
    """An age calculator."""
    age = datetime.datetime.now().year - birthyear
    if birthyear > datetime.datetime.now().year:
        raise InvalidAgeError
    else:
        return age
