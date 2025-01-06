# Create access token
from fastapi import Depends, HTTPException,status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
# from jose import JWTError, jwt

# from app.utils import u_hash
# from app.db import models

import dotenv
CFG = dotenv.dotenv_values(".env")
SECRET_KEY  = CFG['secret']
ALGORITHM   = CFG['algorithm']


# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://localhost:8080/biz_setup/biz_setup_user/token")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="http://99.79.70.8:8080/biz_setup/biz_setup_user/token")

def authent():    return True
