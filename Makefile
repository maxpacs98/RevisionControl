build:
	@git describe --tags --long --dirty --always
	@python hello.py
