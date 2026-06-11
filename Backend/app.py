from flask import Flask
import yfinance as yf
from ta.momentum import RSIIndicator

app = Flask(__name__)


@app.route("/")
def home():
    return "AlgoTrading AI Backend Running"


@app.route("/stock/<symbol>")
def stock_analysis(symbol):

    # Download stock data
    df = yf.download(
        symbol,
        period="3mo"
    )

    # Extract close prices
    close_prices = df["Close"][symbol]

    # Calculate SMA
    df["SMA"] = (
        close_prices
        .rolling(window=5)
        .mean()
    )

    # Calculate EMA
    df["EMA"] = (
        close_prices
        .ewm(span=5)
        .mean()
    )

    # Calculate RSI
    df["RSI"] = RSIIndicator(
        close=close_prices
    ).rsi()

    # Latest values
    latest_price = float(
        close_prices.iloc[-1]
    )

    latest_sma = float(
        df["SMA"]
        .dropna()
        .iloc[-1]
    )

    latest_ema = float(
        df["EMA"]
        .dropna()
        .iloc[-1]
    )

    latest_rsi = float(
        df["RSI"]
        .dropna()
        .iloc[-1]
    )

    # Recommendation Logic
    if latest_rsi < 30:
        signal = "BUY"

    elif latest_rsi > 70:
        signal = "SELL"

    else:
        signal = "HOLD"

    # Return JSON Response
    return {
        "symbol": symbol.upper(),
        "price": round(latest_price, 2),
        "sma": round(latest_sma, 2),
        "ema": round(latest_ema, 2),
        "rsi": round(latest_rsi, 2),
        "recommendation": signal
    }


if __name__ == "__main__":
    app.run(debug=True)