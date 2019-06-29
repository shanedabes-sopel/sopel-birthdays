# coding=utf-8

from __future__ import (unicode_literals, absolute_import,
                        division, print_function)

import itertools

import sopel.module
import sopel.formatting
import requests


def configure(config):
    pass


def setup(bot):
    pass


def get_names(j):
    """ Get names from json response """
    return [i['text'] for i in j['data']['Births']]


def apply_colours(days, colours):
    """ Apply given colours to list of names """
    cdays = [sopel.formatting.color(i, j)
             for i, j in zip(days, itertools.cycle(colours))]

    return cdays


@sopel.module.commands('bdays')
def bdays(bot, trigger):
    r = requests.get('https://history.muffinlabs.com/date')
    rj = r.json()

    names = get_names(rj)

    bot.say(', '.join(names))
