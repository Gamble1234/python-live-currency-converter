# Version_02

"""
📌 Simple Currency Converter (Tkinter)
- Fetches live currency exchange rates using exchangerate.host API
- Provides a GUI for user input (From Currency, To Currency, Amount)
- Displays the converted value in the application window
"""

import tkinter as tk
import requests

# API endpoint and access key (replace with your valid key if required)
API_URL = "https://api.exchangerate.host/convert"
API_KEY = "YOUR API KEY"  # Replace with your exchangerate API key

def convert_currency():
    """
    Convert the entered amount from one currency to another
    using the exchangerate.host API and display result in GUI.
    """
    from_currency = entry_from.get().strip()
    to_currency = entry_to.get().strip()
    amount = entry_amount.get().strip()

    # ✅ Check if fields are empty
    if not from_currency or not to_currency or not amount:
        result_label.config(text="⚠️ Please fill all fields")
        return

    # ✅ Validate amount (must be a number)
    try:
        amount = float(amount)
    except ValueError:
        result_label.config(text="⚠️ Amount must be a number")
        return

    # ✅ API request parameters
    params = {
        "from": from_currency,
        "to": to_currency,
        "amount": amount,
        "access_key": API_KEY
    }
    
    # ✅ Send GET request to API
    response = requests.get(API_URL, params=params)
    data = response.json()

    # ✅ Handle API response
    if data.get("success"):  # If API returned a successful response
        converted = data["result"]
        result_label.config(
            text=f"💱 {amount} {from_currency.upper()} = {converted:.2f} {to_currency.upper()}"
        )
    else:  # If API failed (invalid currency or missing key)
        result_label.config(text="❌ Conversion failed. Check currency codes.")

# ---------------- GUI Setup ----------------
app = tk.Tk()
app.title("Currency Converter")  # App title
app.geometry("350x350")          # Window size

# Input fields
tk.Label(app, text="From Currency (e.g. USD, INR):").pack(pady=5)
entry_from = tk.Entry(app)
entry_from.pack()

tk.Label(app, text="To Currency (e.g. USD, INR):").pack(pady=5)
entry_to = tk.Entry(app)
entry_to.pack()

tk.Label(app, text="Amount:").pack(pady=5)
entry_amount = tk.Entry(app)
entry_amount.pack()

# Convert button
tk.Button(app, text="Convert", command=convert_currency).pack(pady=10)

# Result label (output will be shown here)
result_label = tk.Label(app, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=5)

# Run the GUI application
app.mainloop()
