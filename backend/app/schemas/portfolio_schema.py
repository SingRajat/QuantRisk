from pydantic import BaseModel
from typing import List


class Asset(BaseModel):
    ticker: str
    weight: float


class PortfolioRequest(BaseModel):
    portfolio: List[Asset]
    period: str


class PortfolioResponse(BaseModel):
    risk_level: str
    metrics: dict
    explanation: str