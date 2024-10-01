from pydantic import BaseModel
from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import ID, TEXT, Schema

ID_KEY = 'id'
PRODUCT_NAME_KEY = 'product_name'
DESCRIPTION_KEY = 'description'
LOCATION_KEY = 'location'


CATALOG_SCHEMA = Schema(
    id=ID(stored=True),
    product_name=TEXT(stored=True),
    description=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    location=TEXT(stored=True),
)

# this will be used by the llm to understand the schema of the data
CATALOG_SCHEMA_DESCRIPTIONS = {
    ID_KEY: 'The id of the item.',
    PRODUCT_NAME_KEY: 'The name of the product catalog item/service.',
    DESCRIPTION_KEY: 'The high-level description of the product catalog item.',
    LOCATION_KEY: 'The location/municipality that offers the service.',
}


ALL_SEARCH_FIELDS = (PRODUCT_NAME_KEY, DESCRIPTION_KEY, LOCATION_KEY)


class SearchResult(BaseModel):
    product_name: str
    location: str
