from fastapi import APIRouter, Depends

from apps.api.v1 import r_root
from apps.utils.u_auth import authent

router = APIRouter()

router.include_router(r_root.router,                                        tags=["Root"],      dependencies=[Depends(authent)])


