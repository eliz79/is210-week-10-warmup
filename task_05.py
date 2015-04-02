#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Changing dictionary values."""

from data import SUPERHEROES

print SUPERHEROES

SUPERHEROES['Logan'] = {'Wolverine': 'Weapon X'}

print 'Added Wolverine'

print SUPERHEROES
