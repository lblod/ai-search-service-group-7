from pathlib import Path

import pandas as pd
from tqdm import tqdm
from whoosh.index import create_in

from aisearch.schema import (
    CATALOG_SCHEMA,
    CONDITIONS,
    DESCRIPTION_KEY,
    ID_KEY,
    LOCATION_KEY,
    PRODUCT_ID,
    PRODUCT_NAME_KEY,
    SEARCH_TERM_KEY,
    TARGET_GROUP,
    URL,
)

# paths
DATA_DIR = Path(__file__).parent.parent / 'data'
INDEX_DIR = DATA_DIR / 'index'
INDEX_DIR.mkdir(exist_ok=True, parents=True)
PROD_CATALOG_CSV = DATA_DIR / 'producten_en_diensten_2024-09-13_21-47-37.csv'

# read the product catalog csv file
df = pd.read_csv(PROD_CATALOG_CSV, encoding='MacRoman')

# add an id field
df['id'] = range(1, len(df) + 1)

# do a subselection of the data columns
df_docs = df[
    [
        'id',
        'Naam',
        'Beschrijving',
        'Geografische toepassingsgebieden (NUTS/LAU)',
        'Doelgroep(en)',
        'Zoektermen',
        'Voorwaarden',
        'Bekijk in IPDC',
        'Product id',
    ]
]

# rename the data columns following the index schema
df_docs = df_docs.rename(
    columns={
        'id': ID_KEY,
        'Naam': PRODUCT_NAME_KEY,
        'Beschrijving': DESCRIPTION_KEY,
        'Geografische toepassingsgebieden (NUTS/LAU)': LOCATION_KEY,
        'Doelgroep(en)': TARGET_GROUP,
        'Zoektermen': SEARCH_TERM_KEY,
        'Voorwaarden': CONDITIONS,
        'Bekijk in IPDC': URL,
        'Product id': PRODUCT_ID,
    }
)

# remove stuff between brackets from location column
df_docs['location'] = df_docs['location'].str.replace(r'\s*\(.*?\)', '', regex=True)

# some fields are nan, replace them by empty strings, otherwise whoosh complains
df_docs = df_docs.fillna('')

# convert the dataframe into documents (list of dicts)
docs = list(df_docs.to_dict(orient='index').values())

# create an index and add documents
index = create_in(INDEX_DIR, CATALOG_SCHEMA)
writer = index.writer()
for doc in tqdm(docs):
    try:
        writer.add_document(
            id=str(doc[ID_KEY]),
            product_name=doc[PRODUCT_NAME_KEY],
            description=doc[DESCRIPTION_KEY],
            location=doc[LOCATION_KEY],
            target_group=doc[TARGET_GROUP],
            search_term=doc[SEARCH_TERM_KEY],
            conditions=doc[CONDITIONS],
            url=doc[URL],
            product_id=doc[PRODUCT_ID],
        )
    except Exception as exc:
        # this should not happen, but at least it won't fail our index creation
        print(f'This product item has been skipped: {doc[ID_KEY]}')
        print(exc)
writer.commit()
