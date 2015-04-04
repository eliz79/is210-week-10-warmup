#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Ways to remove or add keys to Python dictionaries."""

import data

CORRECTED = data.BANDS.copy()

CORRECTED.update({'Dylan': {'Bob Dylan': ['vocals', 'guitar', 'harmonica']}})

del CORRECTED['Van Halen']['David Lee Roth']

CORRECTED['Van Halen'].update({'Sammy Hagar': ['vocals']})
