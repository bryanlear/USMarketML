import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = '/Users/bryanlee/Desktop/US_market_data_ML/PredictiveModel/data/raw/market_data/MSFT_86_17_US/msft.us.txt'
df = pd.read_csv(file_path)
df.drop(columns=['OpenInt'], inplace=True)
# Convert the 'Date' column to datetime format
df['Date'] = pd.to_datetime(df['Date'])

# Calculate Q1 (25th percentile) and Q3 (75th percentile)
Q1 = df['Volume'].quantile(0.25)
Q3 = df['Volume'].quantile(0.75)

# Calculate the IQR
IQR = Q3 - Q1

# Define the outlier bounds
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

# Filter the data to remove outliers
df_no_outliers = df[(df['Volume'] >= lower_bound) & (df['Volume'] <= upper_bound)].copy()

# Calculate Daily Returns
df_no_outliers.loc[:, 'Daily Return'] = df_no_outliers['Close'].pct_change()

# Plot the boxplot without outliers
plt.figure(figsize=(10, 5))
plt.boxplot(df_no_outliers['Volume'])
plt.title('Boxplot of Volume (Without Outliers)')
plt.ylabel('Volume')
plt.show()

# Display summary statistics without outliers
print(df_no_outliers.describe())

# Plot the volume without outliers
plt.figure(figsize=(10, 5))
plt.plot(df_no_outliers['Date'], df_no_outliers['Volume'], label='Volume', color='orange')
plt.title('Microsoft Stock Volume Over Time (Without Outliers)')
plt.xlabel('Date')
plt.ylabel('Volume')
plt.legend()
plt.show()

# Plot daily returns without outliers
plt.figure(figsize=(10, 5))
plt.plot(df_no_outliers['Date'], df_no_outliers['Daily Return'], label='Daily Return', color='green')
plt.title('Microsoft Stock Daily Returns (Without Outliers)')
plt.xlabel('Date')
plt.ylabel('Daily Return')
plt.legend()
plt.show()

# Calculate moving averages without outliers
df_no_outliers.loc[:, '20 Day MA'] = df_no_outliers['Close'].rolling(window=20).mean()
df_no_outliers.loc[:, '50 Day MA'] = df_no_outliers['Close'].rolling(window=50).mean()

# Plot closing price and moving averages without outliers
plt.figure(figsize=(10, 5))
plt.plot(df_no_outliers['Date'], df_no_outliers['Close'], label='Closing Price')
plt.plot(df_no_outliers['Date'], df_no_outliers['20 Day MA'], label='20 Day MA', color='red')
plt.plot(df_no_outliers['Date'], df_no_outliers['50 Day MA'], label='50 Day MA', color='purple')
plt.title('Microsoft Stock Closing Price and Moving Averages (Without Outliers)')
plt.xlabel('Date')
plt.ylabel('Price')
plt.legend()
plt.show()

# Correlation analysis without outliers
correlation_matrix_no_outliers = df_no_outliers.corr()
print(correlation_matrix_no_outliers)

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix_no_outliers, annot=True, fmt='.2f', cmap='coolwarm')
plt.title('Correlation Matrix (Without Outliers)')
plt.show()


#Analyze the volatility of the stock using measures like the standard deviation of returns.
df['Rolling Std'] = df['Daily Return'].rolling(window=20).std()

plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Rolling Std'], label='Rolling Std (20 days)', color='red')
plt.title('Microsoft Stock Rolling Standard Deviation of Daily Returns')
plt.xlabel('Date')
plt.ylabel('Rolling Std')
plt.legend()
plt.show()