import typing

from pydanitc import BaseModel


class Product(BaseModel):
    id: int
    name: str
    brand: str
    description: str
    url: str
    image: str
    review_count: int
    average_review: float
    available_in_store: bool = False 
    extras: typing.Optional[typing.Dict] = None


class Store(BaseModel):
    id: int
    name: str
    capabilities: typing.List[str]
    operating_hours: typing.Dict
    is_open: bool = False
    address: str
    contact_information: typing.Dict
    latitude: float
    longitude: float
    extras: typing.Optional[typing.Dict] = None
