from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.database import get_db
from src.models.models import Product, IngredientsProduct

router = APIRouter(
    prefix="/product",
    tags=["Product"]
)


@router.post("/products")
def product_by_id(id_product: int, session: Session = Depends(get_db)):
    stmt = session.query(Product).filter_by(id=id_product).first()
    ingredient = session.query(IngredientsProduct).filter_by(id_product=id_product).all()
    return stmt, ingredient


@router.get("/products")
def all_product(session: Session = Depends(get_db)):
    product = session.query(Product).all()
    return product


@router.get("/ingredient")
def ingredient_by_id_product(id_product: int, session: Session = Depends(get_db)):
    stmt = session.query(IngredientsProduct).filter_by(id_product=id_product).all()
    return stmt
