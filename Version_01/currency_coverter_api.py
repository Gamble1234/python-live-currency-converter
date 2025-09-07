# Version_01

"""
📌 Problem Statement
Create a Python script that converts one currency to another using live exchange rates
from a real-time API (like ExchangeRate-API or exchangerate.host).
"""

import requests

# Function to perform currency conversion using API
def convert_currency(from_currency, to_currency, amount):
    url = "https://api.exchangerate.host/convert"  # API endpoint
    params = {
        "from": from_currency,   # Source currency (e.g., USD)
        "to": to_currency,       # Target currency (e.g., INR)
        "amount": amount,        # Amount to be converted
        "access_key": "YOUR API KEY"  # Replace with your exchangerate API key
    }

    # Send GET request to the API
    response = requests.get(url, params=params)

    # If request is successful
    if response.status_code == 200:
        data = response.json()
        if data.get("success"):  # Check if conversion was successful
            converted = data['result']
            print(f"\n💱 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}")
        else:
            # API returned an error (invalid key or wrong currency code)
            print("❌ Error:", data.get("error", "Unknown issue"))
    else:
        # If API request failed due to server or network issue
        print("❌ Error fetching exchange rates. HTTP code:", response.status_code)


# ---------------- Interactive CLI ----------------
while True:
    # Ask user for source currency
    from_currency = input("\nEnter FROM currency (or type 'exit' or 'quit' or 'q' to quit): ").strip().lower()

    # Exit condition
    if from_currency in ["exit", "quit", "q"]:
        print("\n👋 Exiting Currency Converter. Goodbye!")
        break

    # Ask user for target currency and amount
    to_currency = input("Enter TO currency: ").strip().lower()
    amount = input("Enter the amount: ").strip()

    try:
        # Convert input amount to float (number)
        amount = float(amount)
        convert_currency(from_currency, to_currency, amount)
    except ValueError:
        # Handle invalid number input
        print("⚠️ Please enter a valid number for amount.\n")
