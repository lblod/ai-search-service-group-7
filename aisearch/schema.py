from whoosh.analysis import StemmingAnalyzer
from whoosh.fields import ID, TEXT, Schema

# whoos schema keys
ID_KEY = 'id'
PRODUCT_NAME_KEY = 'product_name'
DESCRIPTION_KEY = 'description'
LOCATION_KEY = 'location'
TARGET_GROUP = 'target_group'
SEARCH_TERM_KEY = 'search_term'
CONDITIONS = 'conditions'
URL = 'url'
PRODUCT_ID = 'product_id'
COSTS = 'costs'

# search results keys
SCORE_KEY = 'score'

CATALOG_SCHEMA = Schema(
    id=ID(stored=True),
    product_name=TEXT(stored=True),
    description=TEXT(stored=True, analyzer=StemmingAnalyzer()),
    location=TEXT(stored=True),
    target_group=TEXT(stored=True),
    search_term=TEXT(stored=True),
    conditions=TEXT(stored=True),
    url=TEXT(stored=True),
    product_id=TEXT(stored=True),
    costs=TEXT(stored=True),
)

# this will be used by the llm to understand the schema of the data
CATALOG_SCHEMA_DESCRIPTIONS = {
    ID_KEY: 'The id of the item.',
    PRODUCT_NAME_KEY: 'The name of the product catalog item/service.',
    DESCRIPTION_KEY: 'The high-level description of the product catalog item.',
    LOCATION_KEY: 'The location/municipality that offers the service.',
    TARGET_GROUP: 'The target group for who this product catalog item is meant for',
    SEARCH_TERM_KEY: (
        'The searching terms where can be searched on to find the product catalog item'
    ),
    CONDITIONS: (
        'These are conditions that someone must meet in order to use this product'
    ),
    URL: 'This is the URL where the product can be found',
    COSTS: 'This is the price of the product',
}

ALL_SEARCH_FIELDS = (
    ID_KEY,
    PRODUCT_NAME_KEY,
    DESCRIPTION_KEY,
    LOCATION_KEY,
    TARGET_GROUP,
    SEARCH_TERM_KEY,
    CONDITIONS,
    URL,
    COSTS,
)

SOURCES_KEYS = [
    PRODUCT_NAME_KEY,
    LOCATION_KEY,
    TARGET_GROUP,
    URL,
    SCORE_KEY,
]
