#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Using dictionary iteration with iteritems()."""

DICT1 = {
    2: 7493945,
    76: 4654320,
    3: 4091979,
    90: 1824881,
    82: 714422,
    45: 1137701,
    0: 326226,
    -15: 417203,
    -56: 333525,
    67: 323451,
    99: 321696,
    21: 336753,
    -100: 361237,
    55: 1209714,
    5150: 1771800,
    42: 4714011,
    888: 14817667,
    3500: 13760234,
    712: 10903322,
    7: 10443792,
    842: 11716264,
    18584: 10559923,
    666: 9275602,
    70: 11901200,
    153: 12074784,
    8: 4337229
}

DICT2 = {
    1: 10,
    2: 20,
    3: 30,
    4: 40,
    5: 50,
    6: 60,
    7: 70,
    8: 80,
    9: 90,
    37: 100
}


def iter_dict_funky_sum(myvar):
    """This is a dictionary iteration using iteritems().

    Arg:
        myvar(int): a running total integer

    Return:
        Will return the funky_total

    Example:
        >>> import task_07
        >>> task_07.iter_dict_funky_sum(DICT1)
        139791890

        >>> import task_07
        >>> task_07.iter_dict_funky_sum(DICT2)
        468
    """
    funky_total = 0
    for key, value in myvar.iteritems():
        funky_total = funky_total + value - key
    return funky_total
