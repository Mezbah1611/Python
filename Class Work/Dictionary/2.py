employee = {
    "Name": "A",
    "Age": "40",
    "Type": {"developer": ["ios", "android"]},  # Removed extra space in "Type"
    "Permanent": True,  # Corrected spelling from "Parmanent" to "Permanent"
    "Salary": 30000,  # Removed extra space in "Salary"
    100: (1, 2, 3),
    4.5: {5.6, True, 7, 1}
}

# Access the "Type" key correctly
x = employee["Type"]  # Corrected access using square brackets and fixed key name
print(x)  # This will print the value associated with the key "Type"
