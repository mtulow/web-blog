import os
from types import SimpleNamespace

def config():
    params = SimpleNamespace(
        user=os.getenv('PG_USER'),
        password=os.getenv('PG_PASSWORD'),
        host=os.getenv('PG_HOST', '0.0.0.0'),
        port=os.getenv('PG_PORT', 5432),
        dbname=os.getenv('PG_DATABASE', 'postgres')
        )
    return params

def database_uri():
    """
    Return the database URI.
    """

    user=os.getenv('PG_USER')
    password=os.getenv('PG_PASSWORD')
    host=os.getenv('PG_HOST', '0.0.0.0')
    port=os.getenv('PG_PORT', 5432)
    dbname=os.getenv('PG_DATABASE', 'postgres')

    return f'postgresql://{user}:{password}@{host}:{port}/{dbname}'