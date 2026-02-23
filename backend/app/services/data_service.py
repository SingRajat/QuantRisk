import yfinance as yf
import pandas as pd
from typing import List


class DataService:

    @staticmethod
    def fetch_adjusted_close(
        tickers: List[str],
        period: str = "1y"
    ) -> pd.DataFrame:
        """
        Fetch adjusted close prices for given tickers.
        Returns clean dataframe indexed by date.
        """

        data = yf.download(
            tickers=tickers,
            period=period,
            auto_adjust=True,
            progress=False
        )

        if data.empty:
            raise ValueError("No data returned from yfinance.")

        # If multiple tickers → multi-index columns
        if isinstance(data.columns, pd.MultiIndex):
            prices = data["Close"]
        else:
            prices = data.to_frame(name=tickers[0])

        # Drop rows with all NaNs
        prices = prices.dropna(how="all")

        return prices