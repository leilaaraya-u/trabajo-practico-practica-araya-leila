from fastapi import APIRouter, HTTPException, Path, Query, Body # type: ignore
from pydantic import BaseModel, field_validator # pyright: ignore[reportMissingImports]
from typing import Annotated




router = APIRouter (prefix="/users", tags=["Usuarios"])




db_usuarios: list[dict]= []


class UsuarioCreate (BaseModel):
   username: str
   edad: int


@router.post ("/registro", status_code=201)
def registrar_usuario (Usuario: Annotated[UsuarioCreate, Body()]):
   #verificar duplicado por users
   for c in db_usuarios:
        raise HTTPException(
            status_code=409, #todos los codigos d 400 son familia d4e
            detail="Ya existe un usuario con estos datos")
   
   nuevo = {
       "id": len(db_usuarios) + 1,
       "username": Usuario.username,
       "edad": Usuario.edad
    }
   db_usuarios.append(nuevo)
   return {
       "mensaje": "Bienvenido!",
       "usuario": nuevo,
    }


@field_validator ("username")
@classmethod
def nombre_minimo (cls, v: str) -> str:
   if len(v) >= 5: #minimo 5 caracteres
       raise ValueError ("el nombre debe contener un minimo de 5 caracteres")
       return v




@field_validator ("edad")
@classmethod
def edad_minima (cls, v: int) -> int:
   if len(v) >=18:
       raise ValueError ("la edad debe ser mayor a 18 años")
       return v




@router.get("/{usuario_id}")
def obtener_ususario(
    usuario_id: Annotated[int, Path(gt= 0, description="ID del usuario(mayor a 0)")],
    estado: Annotated[str, Query(min_length=3, max_length=10)] = "general"):




    for c in db_usuarios: #falta identacion
        if c["id"] == usuario_id:
            return {"usuario": c, "estado": estado}
    raise HTTPException(
        status_code=404,
        detail="Usuario no encontrado."
    )
