import pandas as pd
import numpy as np

# Number variable
age = 42
print("Number Variable:", age)

# String variable
string_variable = "Hello, Alan"
print("String Variable:", string_variable)

# List
my_list = [18, 9, 1, 27, 24]
print("List:", my_list)

# Dictionary
my_dict = {
    "name": "John",
    "age": 34,
    "Medical_history": ["asthma", "high_blood_pressure", "arthritis"], 
    "address": {  # Nested dictionary
        "city": "New York",
        "zipcode": "10001"
    }
}
print("Dictionary:", my_dict)

# Function to analyze white blood cell (WBC) count
def analyze_wbc_count(wbc_count):
    if wbc_count < 4.0:
        result = f"WBC count of {wbc_count} is low."
    elif 4.0 <= wbc_count <= 11.0:
        result = f"WBC count of {wbc_count} is within the normal range."
    else:
        result = f"WBC count of {wbc_count} is high. This might indicate an infection or other medical condition."
    return result

# Run the function and print the result
wbc_result = analyze_wbc_count(8.5)
print("White Blood Cell Count Analysis:", wbc_result)
