from pydantic import BaseModel


class OrderBaseSchema(BaseModel):
    status: str
    id_user: int
    address: str
    delivery: bool
    id_chef: int
    id_couriers: int
    cost: float
    products: list


class OrderSchema(OrderBaseSchema):
    id: int
    id_user: int

    class Config:
        orm_mode = True