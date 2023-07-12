import uvicorn
from fastapi import FastAPI
from src.user.router import router as router_user
from src.order.router import router as router_order
from src.product.router import router as router_product

app = FastAPI()

app.include_router(router_user)
app.include_router(router_order)
app.include_router(router_product)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True, log_level="debug")
