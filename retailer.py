import typing
from abc import ABC, abstract_method

from storie.models import Store, Product


class Retailer(ABC):
    credentials: typing.Dict = {}
    store: models.Store = None

    @abstract_method
    def get_store(self, place: str, store_id: str = None, store_name: str = None) -> Store:
        """ Return a Store object or None given a Taget store_id or store_name that's within the given place.

        Parameters:
            place (str): a single zipcode, name of a city, and or a state
            store_id (str): a valid Target location id (defaults to None)
            store_name (str): a valid Target location name (defaults to None)

        Returns
            store (Store): a Store object if store exists
            None: if store does not exist
        """
        pass

    @abstract_method
    def get_stores(self, place: str, limit: int, within: int) -> typing.List[Store]:
        """ Returns a list of stores within an area of a given place.

        Parameters:
            place (str): a single zipcode, name of a city, and or a state
            limit (int): the number of items returned (defaults to 20)
            within (int): the max range to look in (defaults to 100 miles)

        Returns:
            list: the list of store dictionaries
        """
        pass

    @abstract_method
    def get_product(self, product_id: int) -> Product:
        """ Returns a product from a given product_id.

        Parameters:
            product_id (int): the unique product id used by the retailer

        Returns:
            product (Product): a Product object if it exists
            None: if product does not exist
        """
        pass

    @abstract_method
    def get_products(self,
        store: Store = None,
        category: str = None,
        page: int = 1,
        results_per_page: int = 25
    ) -> typing.List[Product]:
        """ Returns a list of products that match the given parameters.

        Parameters:
            store (Store): the store you wish to search from (defaults to None or the set store)
            category (str): the extact name of the retailer's category you wish to get products from
            page (int): the page number (defaults to 1)
            results_per_page (int): the number of products per page (defaults to 25)

        Returns:
            products (list): a list of Product objects
        """
        pass

    @abstract_method
    def scrape_product(self, product_url: str) -> Product:
        """ Returns a product from a product's url. This method will attempt to scrape the retailer's
        product page.
        
        Parameters:
            product_url (str): the full url to the product you wish to scrape

        Returns:
            product (Product): a product object if it exists
            None: if product does not exist
        """
        pass

    @abstract_method
    def search(self, 
        query: str,
        store: Store = None,
        category: str = None,
        page: int = 1,
        results_per_page: int = 25,
        **filters
    ) -> typing.List[Product]:
        """ Returns a list of products from search results.
        
        Parameters:
            query (str): the search query
            store (Store): the store you wish to search from (defaults to None or the set store)
            category (str): the extact name of the retailer's category you wish to get products from
            page (int): the page number (defaults to 1)
            results_per_page (int): the number of products per page (defaults to 25)
            filters: additional and optional filters specific to the retailer you way use

        Returns:
            products (list): a list of Product objects
        """
        pass
