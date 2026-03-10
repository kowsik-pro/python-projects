import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("data/creditcard.csv")

print("Dataset loaded successfully")
print("Shape of dataset:", df.shape)


print("\nFirst 5 rows:")
print(df.head())


fraud_counts = df["Class"].value_counts()

print("\nFraud vs Normal Transactions:")
print(fraud_counts)


fraud_counts.plot(kind="bar")

plt.title("Fraud vs Normal Transactions")
plt.xlabel("Class (0 = Normal, 1 = Fraud)")
plt.ylabel("Count")

plt.show()

# Transaction amount distribution
df["Amount"].plot(kind="hist", bins=50)

plt.title("Transaction Amount Distribution")
plt.xlabel("Amount")

plt.show()