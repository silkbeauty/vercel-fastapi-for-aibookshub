from fastapi import APIRouter, Depends

from apps.utils.u_auth import authent

router = APIRouter()

# router.include_router(r_system_setup_coa.router,    prefix="/coa",  tags=["System Setup: COA"], dependencies=[Depends(authent)])
# router.include_router(r_system_setup_naics.router,  prefix="/naics",tags=["System Setup: NAICS"], dependencies=[Depends(authent)])

@router.get("/")
def root(): return {"SS": "System Setup"}
