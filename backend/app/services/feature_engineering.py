import pandas as pd
import numpy as np


class FeatureEngineering:

    @staticmethod
    def compute_returns(prices: pd.DataFrame) -> pd.DataFrame:
        return prices.pct_change().dropna()

    @staticmethod
    def compute_portfolio_returns(
        returns: pd.DataFrame,
        weights: np.ndarray
    ) -> pd.Series:
        return returns.dot(weights)

    @staticmethod
    def annualized_volatility(portfolio_returns: pd.Series) -> float:
        return portfolio_returns.std() * np.sqrt(252)

    @staticmethod
    def value_at_risk(portfolio_returns: pd.Series, confidence=0.95) -> float:
        return np.percentile(portfolio_returns, (1 - confidence) * 100)

    @staticmethod
    def max_drawdown(portfolio_returns: pd.Series) -> float:
        cumulative = (1 + portfolio_returns).cumprod()
        peak = cumulative.cummax()
        drawdown = (cumulative - peak) / peak
        return drawdown.min()

    @staticmethod
    def correlation_matrix(returns: pd.DataFrame) -> pd.DataFrame:
        return returns.corr()

    @staticmethod
    def diversification_ratio(
        returns: pd.DataFrame,
        weights: np.ndarray
    ) -> float:
        cov_matrix = returns.cov() * 252
        weighted_vol = np.sqrt(np.dot(weights.T, np.dot(cov_matrix, weights)))
        individual_vol = np.sqrt(np.diag(cov_matrix))
        return np.dot(weights, individual_vol) / weighted_vol