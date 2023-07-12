from typing import Annotated

from fastapi import APIRouter, Body, Depends, HTTPException, status
from sqlalchemy.orm import Session
import jwt

from src.config import SECRET_KEY
from src.database import get_db
from src.schemas.order import OrderBaseSchema
from src.user.router import oauth2_scheme
from src.services.db import order as order_db_services

router = APIRouter(
    prefix="/order",
    tags=["Order"]
)


# @router.post("/order")
# def add_order(token: Annotated[str, Depends(oauth2_scheme)],
#               session: Session = Depends(get_db)):


@router.post('/order')
def add_order(token: Annotated[str, Depends(oauth2_scheme)],
              payload: OrderBaseSchema = Body(),
              session: Session = Depends(get_db),
              ):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        payload.id_user = data["id"]
        products = payload.products
        payload.products = []
        # for i in payload.tags:
        # tags = session.query(Tags).filter(Tags.id.in_(payload.tags)).all()
        # print(type(tags[0]))
        # print(session.query(Tags.name).filter(Tags.id.in_(payload.tags).all()))
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="сорри"
        )
    return order_db_services.create_order(session, order=payload, products=products)
