#!/usr/bin/env python
# coding=utf-8

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import unittest
import pytest

from sopel_modules.birthdays import birthdays


def test_get_names():
    j = {'data': {'Births': [{'text': 'person1'}]}}
    expected = ['person1']

    names = birthdays.get_names(j)

    assert expected == names
