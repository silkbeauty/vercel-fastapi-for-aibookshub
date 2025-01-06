from fastapi import APIRouter, Depends

from apps.api.v1 import r_root, system_setup, biz_setup
from apps.utils.u_auth import authent

router = APIRouter()

router.include_router(r_root.router,                                        tags=["Root"],      dependencies=[Depends(authent)])
# router.include_router(system_setup.router,  prefix="/system_setup", tags=["System Setup"],      dependencies=[Depends(authent)])
# router.include_router(biz_setup.router,     prefix="/biz_setup",    tags=["Biz Entity Setup"],  dependencies=[Depends(authent)])


