"""
def celcius2farenheit(celsius):
    fahrenheit = (9/5) * celsius + 32
    return fahrenheit

def main():
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = celcius2farenheit(celsius)
    print("The temperature is ",fahrenheit," degrees Fahrenheit.")

main()
"""

"""
import requests
apres = requests.get("https://yokai.pythonanywhere.com/price?s=AAPL")
print("3 Apple stocks are", float(apres.text)*3, "dollars")

intelres = requests.get("https://yokai.pythonanywhere.com/price?s=INTC")
print("10 Intel stocks are", float(intelres.text)*10, "dollars")

amdres = requests.get("https://yokai.pythonanywhere.com/price?s=AMD")
print("1 AMD stock is", float(amdres.text)*1, "dollars")
"""

import requests
from concurrent.futures import ThreadPoolExecutor

def get_stock_price(symbol, quantity):
    response = requests.get(f"https://yokai.pythonanywhere.com/price?s={symbol}")
    price = float(response.text)
    total_cost = price * quantity
    return symbol, total_cost, quantity

stocks = [("AAPL", 3), ("INTC", 10), ("AMD", 1)]

with ThreadPoolExecutor() as executor:
    results = list(executor.map(lambda x: get_stock_price(x[0], x[1]), stocks))

sum = 0
for symbol, total_cost, quantity in results:
    sum += total_cost
    print(f"{quantity} {symbol} stocks cost {total_cost:.2f} dollars")

print(f"Total cost: {sum:.2f} dollars")




