import yfinance as yf

# Ticker de Oracle en NYSE
ticker = yf.Ticker("ORCL")

# Información general
info = ticker.info
print("Nombre:", info.get("longName"))
print("Precio de mercado (regular):", info.get("regularMarketPrice"))

# Descargar histórico (últimos 5 años, diario)
hist = ticker.history(period="5y", interval="1d", auto_adjust=True)
print(hist.tail())

# Ejemplo: cierre más reciente
print("Último cierre:", hist['Close'].iloc[-1])
