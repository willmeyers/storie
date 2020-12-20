import typing

from pydantic import BaseModel


class Category(BaseModel):
    name: str
    url: str
    category: typing.Optional[Category] = None


class Item(BaseModel):
    category: Category
    
    name: str
    display_name: str
    diplay_type: str

    sub_brand_name: str

    pln: str
    wic: str
    prod_id: str
    sku_id: int
    upc: str
    gtin: str
    store_upc: str
    ds_sku_id: str
    fsa_cd: str
    
    image_url: str
    product_url: str

    review_count: int
    average_review: str

    price: str
    price_size: str
    product_size: str
    price_info: typing.Dict
    rebate_message: typing.Dict

    main_ingredient: str
    ingredient_list: typing.List[str]

    available_in_store: bool = False
    age_restristed: bool = False
    exclude_local_delivery: bool = False

    same_day_purchase_limt: int

    extras: typing.Optional[typing.Dict] = None


class Store(BaseModel):
    store_id: int
    type_code: str
    type_description: str
    sub_type_code: str
    status: str
    store_names: typing.List[str]
    address: typing.Dict
    contact_information: typing.Dict
    capabilities: typing.List[str]
    building_area: int
    milestones: typing.List[typing.Dict]
    latitude: float
    longitude: float
