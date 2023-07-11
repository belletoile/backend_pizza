from sqlalchemy.orm import Session

from src.models.models import PaymentCard
from src.schemas.card import CardBaseSchema


def create_card(session: Session, card: CardBaseSchema):
    db_card = PaymentCard(**card.dict())
    session.add(db_card)
    session.commit()
    session.refresh(db_card)
    return db_card