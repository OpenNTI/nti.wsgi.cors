import codecs
from setuptools import setup, find_packages

VERSION = '0.0.0'

entry_points = {
	"paste.filter_app_factory": [
		"cors = nti.wsgi.cors:cors_filter_factory",
		"cors_options = nti.wsgi.cors:cors_option_filter_factory",
	],
}

TESTS_REQUIRE = [
	'coverage',	# Test coverage
	'fudge',
	'nose',
	'pyhamcrest',
	'nti.testing',
]

setup(
	name = 'nti.wsgi.cors',
	version = VERSION,
	author = 'Jason Madden',
	author_email = 'jason@nextthought.com',
	description = "Support for CORS in a WSGI environment",
	long_description = codecs.open('README.rst', encoding='utf-8').read(),
	license = 'Proprietary', # This is a candidate for Open Source
	keywords = 'wsgi cors',
	tests_require=TESTS_REQUIRE,
	classifiers = [
		'Intended Audience :: Developers',
		'Natural Language :: English',
		'Operating System :: OS Independent',
		'Programming Language :: Python :: 2',
		'Programming Language :: Python :: 2.7',
		'Programming Language :: Python :: 3',
		'Programming Language :: Python :: 3.3',
	],
	packages=find_packages('src'),
	package_dir={'': 'src'},
	namespace_packages=['nti', 'nti.wsgi'],
	install_requires=[
		'setuptools',
		'greenlet'
	],
	extras_require={
		'test': TESTS_REQUIRE,
	},
	entry_points=entry_points
)
