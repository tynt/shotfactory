pep8 :
	pep8.py --filename=*.py --repeat .

pylint :
	pylint shotfactory04 \
	| grep -v "test_suite\.test_"
