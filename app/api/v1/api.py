from app import api
from fastapi import APIRouter

from app.api.v1.views import user
from app.api.v1.views import production_device
from app.api.v1.views import production_data
from app.api.v1.views import welding_data
from app.api.v1.views import real_time_monitoring



api_router = APIRouter()

api_router.include_router(user.router, tags=['user'], prefix='/auth')
api_router.include_router(production_device.router, tags=['生产设备管理'], prefix='/auth')
api_router.include_router(production_data.router, tags=['生产数据统计'], prefix='/auth')
api_router.include_router(welding_data.router, tags=['焊接数据统计'], prefix='/auth')
api_router.include_router(real_time_monitoring.router, tags=['实时数据'], prefix='/auth')