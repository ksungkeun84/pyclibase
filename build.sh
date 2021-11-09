
python3 -m build
python3 -m twine upload --repository pypi dist/*
conda skeleton pypi pyclibase
conda-build pyclibase
