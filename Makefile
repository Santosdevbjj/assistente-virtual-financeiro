install:
	pip install -r src/requirements.txt

run:
	streamlit run src/app.py

test:
	pytest -q

validate:
	python scripts/validate_data.py

all: validate test
