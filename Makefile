pep8 :
	pep8.py --filename=*.py --repeat .

pylint :
	pylint shotfactory04 \
	| grep -v "test_suite\.test_"

doctest :
	grep -rl --include "*.py" "doctest.testmod()" . | xargs -n1 python
