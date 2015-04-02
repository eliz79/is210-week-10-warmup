#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Merging a dictionary."""

from data import BANDS

BANDS['Fleetwood Mac'].update({
    'Buckingham Nicks': {
        'Lindsey Buckingham': ['guitar', 'vocals'],
        'Steve Nicks': ['vocals', 'tambourine'],
        }})
