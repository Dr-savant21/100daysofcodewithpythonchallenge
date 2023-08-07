import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the dataset into a Pandas DataFrame
df = pd.read_csv("cars.csv")

# Display the first few rows of the dataset
print(df.head())

# Data cleaning
# Drop rows with missing values
df.dropna(inplace=True)

# Data filtering
# Filter cars with a mileage greater than 100,000
filtered_df = df[df["mileage"] > 100000]

# Data aggregation
# Calculate the average price by car make
average_price_by_make = df.groupby("make")["price"].mean()

# Data visualization
# Plot a histogram of car prices
plt.hist(df["price"], bins=20)
plt.xlabel("Price")
plt.ylabel("Frequency")
plt.title("Distribution of Car Prices")
plt.show()

# Display the average price by car make
print(average_price_by_make)
