import typing

from pydantic import BaseModel


class Category(BaseModel):
    name: str
    code: str
    path: str
    category: typing.Optional[Category] = None


class Product(BaseModel):
    category: Category
    
    name: str
    brand: str
    bullet_descriptions: typing.List[str]
    soft_bulltets: List[str]
    buy_url: str
    price: float

    primary_image_url: str
    alternate_image_urls: typing.List[str]

    tcin: int
    tcin_original: int
    merch_class_id: int
    merch_department_id: int
    dcpi: int

    vendors: List[str]

    only_at_taget: bool = False
    promotions: List[Dict]

    average_rating: float
    number_of_ratings: int
    secondary_ratings: typing.List[Dict]

    available_in_store: bool = False

    extras: typing.Optional[typing.Dict] = None


class Store(BaseModel):
    store_id: int
    type_code: str
    type_description: str
    sub_type_code: str
    status: str
    name: str
    address: typing.Dict
    contact_information: typing.Dict
    capabilities: typing.List[str]
    building_area: int
    milestones: typing.List[typing.Dict]
    latitude: float
    longitude: float
