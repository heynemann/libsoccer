clear:
	@find . -name '*.pyc' -delete

stats:
	@pyflakes libsoccer/*.py
	@pylint libsoccer

test: clear
	@nosetests -v -s --with-coverage --cover-erase --cover-inclusive --cover-package=libsoccer tests/
