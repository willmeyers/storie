import typing

import requests

from storie.retailer import Retailer
from storie.models import Product, Store
from storie.target import config


class Target(Retailer):
    def __init__(self, get_closest_store_to: str = None, key: str = None, visitor_id: str = None):
        self.credentials['user_agent'] = '{"User-Agent": ""}'
        self.credentials['key'] = key if key else 'ff457966e64d5e877fdbad070f276d18ecec4a01'
        self.credentials['visitor_id'] = visitor_id if visitor_id else '01767696FA7D020198F9B21FFADB8E8D'

        if get_closest_store_to:
            self.store = self.get_store(get_closest_store_to)

    def _format_store_address(self, addr: typing.Dict) -> str:
        """ Formats Target's store address JSON response into a human-friendly string.
        """
        
        return f"{addr['address_line1']} {addr['city']} {addr['region']} {addr['postal_code']}"

    def _format_store_contact_information(self, info: typing.Dict) -> typing.Dict:
        """ Format Target' store contact information into a human-friendly dictionary.
        """
        
        return {
            'phone_number': info['telephone_number']
        }

    def get_store(self, place: str, id: int = None, name: str = None) -> Store:
        stores = self.get_stores(place)

        for store in stores:
            if id:
                if store._id == store_id:
                    return stores

            if name:
                if name.lower() == store.name.lower():
                    return store
                    

        return stores[0] if stores else None

    def get_stores(self, place: str, int = 20, within: int = 100) -> typing.List[Store]:
        url = f'{config.TARGET_REDSKY_BASE_URL}/v3/stores/nearby/{place}'

        resp = requests.post(url, 
            params={
                'key': self.key,
                'limit': limit,
                'within': within,
                'unit': 'mile'
            }
        )

        stores = []
        for store in resp.json():
            store_extras = {
                'type_code': store['type_code'],
                'type_description': store['type_description'],
                'sub_type_code': store['sub_type_code'],
                'physical_specifications': store['physical_specifications']
            }

            stores.append(Store(
                    id=store['store_id'],
                    name=store['store_names'][0]['name'].title(),
                    is_open=True if store['status'] == 'Open' else False,
                    capabilities=[s['capability_name'] for s in store['capabilities']],
                    contact_information=s['contact_information'],
                    milestones=store['milestones'],
                    latitude=store['geographic_specification']['latitude'],
                    longitude=store['geographic_specification']['longitude'],
                    address=self._format_store_address(store['address']),
                    contact_information=self._format_store_contact_information(store['contact_information']),
                    extras=store_extras
                )
            )

        return stores

    def get_product(self, id: int, store: Store = None) -> Store:
        pass

    def get_products(self,
        store: Store = None,
        category: str = None,
        page: int = 1,
        results_per_page: int = 25
    ) -> typing.List[Product]:
        pass

    def search(self, query: str) -> typing.List[Product]:
        pass

    def get_trending_searches(self):
        pass

    def get_deals(self):
        pass

    def get_promotions(self):
        pass
