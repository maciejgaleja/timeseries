coverage:
	coverage run test.py
	coverage html
	coverage report -m --fail-under=100
