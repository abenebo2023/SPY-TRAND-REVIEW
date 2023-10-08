import matplotlib.pyplot as plt
import pandas as pd
import yfinance as yf
import time
import datetime
import csv
import requests
from urllib3.util import url

# Define the stock symbol (e.g., SPY for S&P 500 ETF)
stock_symbol = 'SPY'

try:
    response = requests.get(url, timeout=10)  # Increase the timeout value (e.g., 10 seconds)
    # Process the response here
except requests.exceptions.Timeout:
    print("Request timed out. Increase the timeout value.")
except requests.exceptions.RequestException as e:
    print(f"An error occurred: {e}")

# Define the time interval (in seconds) for fetching option chain data
interval_seconds = 100  # 15 minutes interval (900 seconds)


def calculate_start_date(end_date, interval_days):
    return end_date - datetime.timedelta(days=interval_days)


while True:
    end_date = datetime.date.today()

    # Fetch the option chain data by calling the function
    option_chain_data = yf.Ticker(stock_symbol).option_chain

    # Access call options
    call_options = option_chain_data().calls
    print("Call Options:")
    print(call_options)

    # Access put options
    put_options = option_chain_data().puts
    print("\nPut Options:")
    print(put_options)

    # Sleep for the specified interval before fetching data again
    time.sleep(5)

# Define the date range for historical data
analysis_interval_seconds = 900  # 15 minutes interval (900 seconds)

while True:
    end_date = datetime.date.today()
    start_date = calculate_start_date(end_date, 7)  # Analyze the last 30 days, for example

    # Fetch historical stock data using yfinance
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)

    # Add your analysis code here for the defined date range

    # Sleep for the specified interval before performing the analysis again
    time.sleep(analysis_interval_seconds)

# Calculate 50-day and 200-day moving averages
stock_data['50_Day_MA'] = stock_data['Adj Close'].rolling(window=50).mean()
stock_data['200_Day_MA'] = stock_data['Adj Close'].rolling(window=200).mean()

# Data Analysis and Visualization
plt.figure(figsize=(12, 6))
plt.title(f'{stock_symbol} Stock Price and Moving Averages')
plt.plot(stock_data.index, stock_data['Adj Close'], label='Adjusted Close', color='blue', alpha=0.7)
plt.plot(stock_data.index, stock_data['50_Day_MA'], label='50-Day MA', color='orange')
plt.plot(stock_data.index, stock_data['200_Day_MA'], label='200-Day MA', color='red')

# Add trend direction annotations
last_50_ma = stock_data['50_Day_MA'].iloc[-1]
last_200_ma = stock_data['200_Day_MA'].iloc[-1]

if last_50_ma > last_200_ma:
    trend_direction = 'Uptrend'
else:
    trend_direction = 'Downtrend'

plt.annotate(f'Trend: {trend_direction}', xy=(stock_data.index[-1], stock_data['Adj Close'].iloc[-1]),
             xytext=(-100, 50),
             textcoords='offset points', arrowprops=dict(arrowstyle='->', color='green'))

plt.legend()
plt.grid()
plt.show()

# Define your capital (the amount you're willing to risk per trade)
capital = 10000  # Example: $10,000

# Define the maximum risk percentage per trade
risk_percentage = 2  # Example: 2% risk per trade

# Calculate the maximum amount you're willing to risk per trade
max_risk_per_trade = (capital * risk_percentage) / 100

# Define the stop-loss percentage for your options trades
stop_loss_percentage = 5  # Example: 5% stop-loss

# Calculate the maximum acceptable loss per trade based on stop-loss
max_loss_per_trade = (capital * stop_loss_percentage) / 100

# Example trade details
option_price = 100  # Price of the option contract
number_of_contracts = 2  # Number of option contracts you plan to buy
entry_price = option_price * number_of_contracts  # Total cost of the option position

# Check if the trade exceeds your maximum risk
if entry_price > max_risk_per_trade:
    print("Trade exceeds maximum risk. Adjust your position size or risk tolerance.")
else:
    print("Trade is within acceptable risk limits.")

# Calculate and check if the potential loss exceeds your stop-loss
potential_loss = (entry_price - option_price) * number_of_contracts  # Assumes options expire worthless
if potential_loss > max_loss_per_trade:
    print("Potential loss exceeds maximum acceptable loss. Consider adjusting your trade.")
else:
    print("Potential loss is within acceptable limits.")

# Define your initial capital and maximum risk percentage per trade
initial_capital = 10000  # Example: $10,000
risk_percentage = 2  # Example: 2% risk per trade

# Define the maximum amount you're willing to risk per trade
max_risk = (initial_capital * risk_percentage) / 100

# Define your entry price, stop-loss price, and target price for an options trade
entry_price = 150  # Example: Entry price of the option
stop_loss_price = 140  # Example: Price at which you'll exit if the trade goes against you
target_price = 170  # Example: Price at which you'll take profits

# Calculate the position size based on the maximum risk
position_size = max_risk / (entry_price - stop_loss_price)

# Calculate the potential profit and potential loss
potential_profit = position_size * (target_price - entry_price)
potential_loss = position_size * (entry_price - stop_loss_price)

# Calculate the risk-reward ratio
risk_reward_ratio = potential_profit / potential_loss

# Check if the risk-reward ratio is acceptable (e.g., >= 2 is often recommended)
if risk_reward_ratio >= 2:
    print("Trade is acceptable with a good risk-reward ratio.")
else:
    print("Trade does not meet the recommended risk-reward ratio.")

# Print the calculated values
print(f"Position Size: {position_size:.2f}")
print(f"Potential Profit: ${potential_profit:.2f}")
print(f"Potential Loss: ${potential_loss:.2f}")
print(f"Risk-Reward Ratio: {risk_reward_ratio:.2f}")

# Fetch the option chain data
option_chain_data = yf.Ticker(stock_symbol).option_chain

# Access call options
call_options = option_chain_data().calls
print("Call Options:")
print(call_options)

# Access put options
put_options = option_chain_data().puts
print("\nPut Options:")
print(put_options)

# Create a DataFrame with hypothetical events
events_data = pd.DataFrame({
    'Event Date': ['2023-10-15', '2023-11-02', '2023-12-05'],
    'Event Description': ['Economic Report A', 'Earnings Report B', 'Geopolitical Event C']
})

# Define the time interval (in seconds) for analyzing events
analysis_interval_seconds = 900  # 15 minutes interval (900 seconds)

while True:
    end_date = datetime.date.today()
    start_date = calculate_start_date(end_date, 30)  # Analyze the last 30 days, for example

    # Filter events within the specified date range
    filtered_events = events_data[(events_data['Event Date'] >= start_date) & (events_data['Event Date'] <= end_date)]

    # Print the relevant events for the specified stock symbol
    print(f"Events affecting {stock_symbol} between {start_date} and {end_date}:\n")
    print(filtered_events)

    # Sleep for the specified interval before analyzing events again
    time.sleep(analysis_interval_seconds)

# Define variables based on your analysis
is_uptrend = True  # Replace with your analysis result
recommended_strategy = None

# Generate recommendations based on the analysis
if is_uptrend:
    recommended_strategy = "Bullish options strategy"
else:
    recommended_strategy = "Bearish options strategy"

# Print the recommendation
print("Recommendation:")
print(recommended_strategy)

# Fetch the current stock price
current_price = yf.Ticker(stock_symbol).info['last_price']

# Define your options position details
option_symbol = 'SPY'  # Replace with your specific option symbol
initial_position = 1  # Number of contracts you initially bought
initial_cost = 1000  # Initial cost of the options position

# Monitor the options position
while True:
    # Fetch the current stock price
    current_price = yf.Ticker(stock_symbol).info['last_price']

    # Calculate the current position value
    current_value = current_price * initial_position

    # Calculate the profit or loss
    profit_or_loss = current_value - initial_cost

    # Print the current position status
    print(f"Current Position Value: ${current_value:.2f}")
    print(f"Profit/Loss: ${profit_or_loss:.2f}")

    # Check if adjustments are needed (e.g., implement a stop-loss or take-profit strategy)
    # Add your adjustment logic here

    # Sleep for a specified interval before checking again (e.g., every 15 minutes)
    time.sleep(900)  # 900 seconds = 15 minutes

# Define the CSV file where you want to record your trades
csv_file = 'options_trades.csv'

# Define trade details (replace with your actual trade details)
trade_date = datetime.date(2023, 10, 15)
option_symbol = 'SPY'
position_type = 'Call Option'
strike_price = 320
expiration_date = datetime.date(2023, 1, 23)
contracts = 5
entry_price = 10.00
exit_price = 15.00
profit_or_loss = exit_price - entry_price

# Create a new row with trade details
trade_record = [trade_date, stock_symbol, option_symbol, position_type, strike_price, expiration_date, contracts,
                entry_price, exit_price, profit_or_loss]

# Append the trade record to the CSV file
with open(csv_file, mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(trade_record)

# Print a confirmation message
print("Trade recorded successfully.")
