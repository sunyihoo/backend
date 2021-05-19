from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1 import api
from app.core.config import settings


app = FastAPI()


# 注册路由
app.include_router(api.api_router,
                #    prefix=settings.API_V1_STR
                   )


# 设置跨域请求

origins = ['*']
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],

    
)


@app.get('/')
def root():
    return {"message": "Hello World!"}
