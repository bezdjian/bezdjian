import sys

import requests

from sb_cal import SalaryCalculator

calc = SalaryCalculator()
# Define the API endpoint URL
url = "https://www7.skatteverket.se/portal-wapi/open/skatteberakning/v1/api/skattetabell/2025/beraknaSkatteavdrag"

default_rate = 800
salary = 60000
hourly_rate = 0

# input
if len(sys.argv) < 2:
    print("Missing arguments. Usage: 'sbc <hours>', OR  'sbc <hours> <hourly rate>")
    sys.exit()  # Use sys.exit() to actually exit the program

if len(sys.argv) == 2:
    hourly_rate = float(default_rate)  # Default rate
elif len(sys.argv) == 3:
    hourly_rate = float(sys.argv[2])

hours = float(sys.argv[1])

salary_with_bonus = calc.calculate_salary_with_bonus(hours, hourly_rate)

# Make the POST request
# Define the request body (data to send)
data = {
    "skattesats": 32,
    "inkomst": salary_with_bonus,
    "fodelsear": 1987,
    "typ": "L"
}
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    tax_deduction = float(response.json().get("skatteavdrag", "N/A"))
    print(f"Calculated tax deduction: {tax_deduction}")
    salary_after_tax = float(response.json().get("lonefterskatt", "N/A"))
    print(f"Net salary with bonus after tax: {salary_after_tax}")
else:
    print(f"POST request failed with status code: {response.status_code}")
    print("Response:", response.text)
