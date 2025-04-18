from fastapi import FastAPI
from app.features.produtos.routes import router as produto_router

app = FastAPI(title="Backend catalog")

# Registra suas rotas de produto/categoria em /api/*
app.include_router(produto_router, prefix="/api")

# Health check na raiz da API
@app.get("/health")
async def health():
    return {"status": "ok", "message": "API funcionando corretamente"}
