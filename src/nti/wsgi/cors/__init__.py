#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
High-level CORS middleware APIs.
"""

from __future__ import print_function, absolute_import, division
__docformat__ = "restructuredtext en"

__all__ = [
    'cors_filter_factory',
    'cors_option_filter_factory',
]

from nti.wsgi.cors.cors import cors_filter_factory
from nti.wsgi.cors.cors import cors_option_filter_factory
