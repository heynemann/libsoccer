clear:
	@find . -name '*.pyc' -delete

test:
	@nosetests -v -s --with-coverage --cover-erase --cover-inclusive --cover-package=libsoccer tests/
