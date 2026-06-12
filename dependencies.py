from fastapi import FastAPI, HTTPException, Query # type: ignore
from typing import Annotated




def verify_api_token(token:Annotated[str, Query()]):
   if token != "nivel-intermedio-2026":
       raise HTTPException(
           status_code=403,
           detail="accedo denegado: token invalido"
       )
       return token
