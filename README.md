# ai-search-service-group-7

## local development setup

Setting up the virtual environment with the right requirements:
```
# setup venv
python3 -m venv .venv
# activate venv
source .venv/bin/activate
# upgrade base requirements
python -m pip install -U pip wheel
# install requirements
python -m pip install -r requirements-dev.txt
# setup pre-commit hooks
pre-commit install
```

create a .env file with the link to the index folder:
```
WHOOSH_INDEX_PATH=<link to index path>
```