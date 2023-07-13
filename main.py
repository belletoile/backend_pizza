import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from src.user.router import router as router_user
from src.order.router import router as router_order
from src.product.router import router as router_product

app = FastAPI()

origins = [

]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["GET", "POST", "DELETE", "OPTIONS"],
    allow_headers=["Content-Type", "Set-Cookie", "Access-Control-Allow-Headers",
                   "Access-Control-Allow-Origin",
                   "Authorization", "Origin", "Accept"],
)

app.include_router(router_user)
app.include_router(router_order)
app.include_router(router_product)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True, log_level="debug")
