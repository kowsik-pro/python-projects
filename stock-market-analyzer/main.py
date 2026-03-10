import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/AAPL.csv")

print("Dataset shape:", df.shape)
print(df.head())

# Convert date column
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date
df = df.sort_values("Date")

# Calculate moving averages
df["MA50"] = df["Close"].rolling(window=50).mean()
df["MA200"] = df["Close"].rolling(window=200).mean()

# Plot stock price
plt.figure(figsize=(10,5))

plt.plot(df["Date"], df["Close"], label="Close Price")
plt.plot(df["Date"], df["MA50"], label="50 Day MA")
plt.plot(df["Date"], df["MA200"], label="200 Day MA")

plt.title("Apple Stock Price Analysis")
plt.xlabel("Date")
plt.ylabel("Price")

plt.legend()

plt.show()