from pathlib import Path

import pandas as pd
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

DATA_DIR = Path(__file__).parent.parent / 'data'
INDEX_DIR = DATA_DIR / 'index'
INDEX_DIR.mkdir(exist_ok=True, parents=True)
PROD_CATALOG_CSV = DATA_DIR / 'producten_en_diensten_2024-09-13_21-47-37.csv'

df = pd.read_csv(PROD_CATALOG_CSV, encoding='MacRoman')
df['id'] = range(1, len(df) + 1)


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
# remove stuff between brackets from location
df_docs['location'] = df_docs['location'].str.replace(r'\s*\(.*?\)', '', regex=True)

print(df_docs.head())
print(df_docs[:3].to_dict(orient='index'))
docs = list(df_docs.to_dict(orient='index').values())

# print(docs)

schema = CATALOG_SCHEMA

ix = create_in(INDEX_DIR, schema)
writer = ix.writer()
for doc in docs:
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
    except Exception:
        pass
        print('This product item has been skipped')
writer.commit()

# print(dir(writer))
