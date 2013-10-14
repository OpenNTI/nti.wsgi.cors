#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""


$Id$
"""

from __future__ import print_function, unicode_literals, absolute_import
__docformat__ = "restructuredtext en"

logger = __import__('logging').getLogger(__name__)

#disable: accessing protected members, too many methods
#pylint: disable=W0212,R0904


from hamcrest import assert_that
from hamcrest import is_
from hamcrest import has_key
from hamcrest import has_entry

import nti.testing.base

from webtest import TestApp

from ..cors import cors_filter_factory
from ..cors import cors_option_filter_factory

from paste.exceptions.errormiddleware import ErrorMiddleware

def test_expected_exceptions_still_have_cors():

	def raises_app( environ, start_response ):
		raise IOError('bad')

	catching_app = ErrorMiddleware( raises_app )
	app = cors_filter_factory( catching_app )

	testapp = TestApp( app )
	res = testapp.get( b'/the_path_doesnt_matter', status=500 )

	assert_that( res.normal_body, is_( 'Failed to handle request bad') )

	# Errors set the right response headers
	res = testapp.get( b'/',
					   extra_environ={b'HTTP_ORIGIN': b'http://example.org'},
					   status=500 )
	assert_that( res.headers, has_key( 'Access-Control-Allow-Origin' ) )

def test_option_handler():

	def raises_app( environ, start_response ):
		raise IOError('bad')

	option_app = cors_option_filter_factory( raises_app )
	app = cors_filter_factory( option_app )


	testapp = TestApp( app )
	res = testapp.options( b'/the_path_doesnt_matter',
						   extra_environ={b'HTTP_ORIGIN': b'http://example.org'},
						   status=200 )

	assert_that( res.headers, has_key( 'Access-Control-Allow-Methods' ) )

	# Non-options pass through
	res = testapp.get( b'/',
					   extra_environ={b'HTTP_ORIGIN': b'http://example.org'},
					   status=500 )
	assert_that( res.headers, has_key( 'Access-Control-Allow-Origin' ) )
