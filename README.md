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

## testing
You can test the deployed endpoint here:
```
# test the ai-search/question endpoint using this curl command
curl -X POST https://lpdc.hackathon-ai-7.s.redhost.be/ai-search/question \
     -H "Content-Type: application/json" \
     -d '{"question":"hoeveel kost een voorlopig rijbewijs in aarschot?"}'
```

Running unittests can be done locally:
```
# run all tests
pytest
# run a specific test
pytest tests/test_search.py
```

