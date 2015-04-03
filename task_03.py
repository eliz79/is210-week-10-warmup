#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Ways to remove or add keys to Python dictionaries."""

import data

CORRECTED = data.BANDS.copy()

CORRECTED.update({'Dylan': {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}})

print CORRECTED

print CORRECTED['Van Halen']

del CORRECTED['Van Halen']['David Lee Roth']

print CORRECTED['Van Halen']

CORRECTED['Van Halen'].update({'Sammy Hagar': ['vocals']})

print CORRECTED['Van Halen']
