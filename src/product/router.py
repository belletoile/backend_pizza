from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
import jwt

from src.database import get_db
from src.models.models import Product

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@router.post("/products")
def product_by_id(id_product: int, session: Session = Depends(get_db)):
    stmt = session.query(Product).filter_by(id=id_product).first()
    return stmt


@router.get("/products")
def all_product(session: Session = Depends(get_db)):
    stmt = session.query(Product).all()
    return stmt