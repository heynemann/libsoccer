clear:
	@find . -name '*.pyc' -delete

test: clear
	@nosetests -v -s --with-coverage --cover-erase --cover-inclusive --cover-package=libsoccer tests/
