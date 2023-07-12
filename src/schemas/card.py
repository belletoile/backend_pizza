from pydantic import BaseModel


class CardBaseSchema(BaseModel):
    card_number: str
    date: str
    id_user: int
    cvc: int


class CardSchema(CardBaseSchema):
    id: int
    id_user: int

    class Config:
        orm_mode = True
