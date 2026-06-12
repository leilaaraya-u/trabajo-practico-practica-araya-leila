from fastapi import FastAPI, Depends # type: ignore
from routers import usuarios, productos
from dependencies import verify_api_token


app = FastAPI(
    title = "sistema de Productos y Usuarios",
    descripcion="API modular con FastAPI - guia complementaria",
    version="1.0.0",
)


app.include_router(usuarios.router)
app.include_router(
    productos.router,
    dependencies=[Depends (verify_api_token)],
)


@app.get("/", tags=["Root"])
def root():
    return{"mensaje": "API de productos funcionando correctamente"}
