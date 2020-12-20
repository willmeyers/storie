import typing

import requests

from . import config, models


class Walgreens:
    api_key: str = None
    aff_id: str = None

    store: models.Store = None

    def __init__(self, api_key: str = None, ):
        pass

    def get_store(self, place: str, store_id: int = None):
        pass

    def get_stores(self, lnglat: typing.Tuple = None, zipcode: int = None, limit: int = 10, within: int = 20):
        pass

    def get_product(self):
        pass

    def get_products(self):
        pass

    def get_offers(self):
        pass
