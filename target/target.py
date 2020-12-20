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

    def get_store(self, place: str, id: int = None, name: str = None) -> models.Store:
        stores = self.get_stores(place)

        for store in stores:
            if store_id:
                if store._id == store_id:
                    return stores

            if store_name:
                for name in store.store_names:
                    if store_name.lower() in name.lower():
                        return store

        return stores[0] if stores else None

    def get_stores(self, place: str, int = 20, within: int = 100) -> typing.List[models.Store]:
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
            stores.append(models.Store(
                    store_id=store['store_id'],
                    type_code=store['type_code'],
                    type_description=store['type_description'],
                    sub_type_code=store['sub_type_code'],
                    status=store['status'],
                    store_names=[s['name'] for s in store['store_names']],
                    address=store['address'],
                    capabilities=[s['capability_name'] for s in store['capabilities']],
                    building_area=s['physical_specifications']['total_building_area'],
                    contact_information=s['contact_information'],
                    milestones=store['milestones'],
                    latitude=store['geographic_specification']['latitude'],
                    longitude=store['geographic_specification']['longitude']
                )
            )

        return stores

    def get_product(self, product_id: int):
        pass

    def get_products(self):
        pass

    def get_trending_searches(self):
        pass

    def get_deals(self):
        pass

    def get_promotions(self):
        pass
