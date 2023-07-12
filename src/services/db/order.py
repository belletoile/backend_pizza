from sqlalchemy.orm import Session

from src.models.models import Order, Product
from src.schemas.order import OrderBaseSchema


def create_order(session: Session, order: OrderBaseSchema, products):
    db_order = Order(**order.dict())
    for t in products:
        tag = session.query(Product).filter_by(id=t).first()
        db_order.products.append(tag)
    session.add(db_order)
    session.commit()
    session.refresh(db_order)
    db_order.products
    return db_order
