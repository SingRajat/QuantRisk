from fastapi import FastAPI
from app.routes.portfolio_routes import router as portfolio_router

app = FastAPI(
    title="AI Portfolio Risk Monitor",
    version="1.0.0"
)

app.include_router(portfolio_router)


@app.get("/health")
def health_check():
    return {"status": "ok"}