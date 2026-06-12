from fastapi import APIRouter, Depends, HTTPException # type: ignore
from pydantic import BaseModel, field_validator # type: ignore
from typing import Annotated
from dependencies import verify_api_token
import re


router= APIRouter (prefix="/productos", tags=["Productos"]) # type: ignore


db_productos: list[dict] = []


class ProductosCreate(BaseModel):
    usuario_id: int


    @field_validator("usuario_id")
    @classmethod
    def id_positivo(cls, v: int) -> int:
        if v  <= 0:
            raise ValueError("usuario_id debe ser mayor a 0")
        return v
   
   
@router.post("/reservar", status_code=201)
def reservar_producto(
    productos: Annotated[ProductosCreate, None],
    _:Annotated[None, Depends (verify_api_token)],
):
    nuevo= {
        "id" : len(db_productos) + 1,
        **productos.model_dump(),
    }
    db_productos.append(nuevo)
    return {"mensaje": "Productos reservados exitosamente", "producto": nuevo}


@router.get("/listar")
def listar_productos():
    return {"total": len(db_productos), "productos": db_productos}
