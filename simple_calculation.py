import sys

import requests

from sb_cal import SalaryCalculator

calc = SalaryCalculator()
# Define the API endpoint URL
url = "https://www7.skatteverket.se/portal-wapi/open/skatteberakning/v1/api/skattetabell/2025/beraknaSkatteavdrag"

# input
if len(sys.argv) < 2:
    print("Missing arguments. Usage: 'stc <salary>'")
    sys.exit()  # Use sys.exit() to actually exit the program

if len(sys.argv) == 1:
    salary = float(sys.argv[1])

salary = int(round(float(sys.argv[1]), 2))
print(f"Net Salary: {salary}")

# Make the POST request
# Define the request body (data to send)
data = {
    "skattesats": 32,
    "inkomst": salary,
    "fodelsear": 1987,
    "typ": "L"
}
response = requests.post(url, json=data)

# Check if the request was successful
if response.status_code == 200:
    tax_deduction = float(response.json().get("skatteavdrag", "N/A"))
    print(f"Calculated tax deduction: {tax_deduction}")
    salary_after_tax = float(response.json().get("lonefterskatt", "N/A"))
    print(f"Net salary after tax: {salary_after_tax}")
else:
    print(f"POST request failed with status code: {response.status_code}")
    print("Response:", response.text)
