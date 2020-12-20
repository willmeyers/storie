import typing
from abc import ABC, abstract_method

from . import models


class Retailer(ABC):
    credentials: typing.Dict = {}
    store: models.Store = None

    @abstract_method
    def get_store(self):
        pass

    @abstract_method
    def get_stores(self):
        pass

    @abstract_method
    def get_product(self):
        pass

    @abstract_method
    def get_products(self):
        pass

    @abstract_method
    def scrape_product(self):
        pass

    @abstract_method
    def search(self):
        pass
