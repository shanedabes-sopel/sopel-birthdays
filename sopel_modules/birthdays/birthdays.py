# coding=utf-8

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

from sopel import module
import requests


def configure(config):
    pass


def setup(bot):
    pass


def get_names(j):
    return [i['text'] for i in j['data']['Births']]


@module.commands('bdays')
def bdays(bot, trigger):
    r = requests.get('https://history.muffinlabs.com/date')
    rj = r.json()
