from app.services.data_service import DataService

if __name__ == "__main__":
    prices = DataService.fetch_adjusted_close(
        ["AAPL", "MSFT"],
        period="1y"
    )

    print(prices.head())