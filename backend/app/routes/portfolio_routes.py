from fastapi import APIRouter
from app.schemas.portfolio_schema import (
    PortfolioRequest,
    PortfolioResponse
)

router = APIRouter(prefix="/portfolio", tags=["Portfolio"])


@router.post("/analyze", response_model=PortfolioResponse)
def analyze_portfolio(request: PortfolioRequest):
    
    # Temporary dummy response
    return PortfolioResponse(
        risk_level="Medium",
        metrics={
            "volatility": 0.18,
            "var_95": -0.04,
            "max_drawdown": -0.22
        },
        explanation="This is a placeholder explanation. Risk engine not yet implemented."
    )