from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm


router = APIRouter(prefix="/oauth", tags=["Auth"])


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):

    pass

