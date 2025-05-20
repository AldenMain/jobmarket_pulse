import pandas as pd
from datetime import date
import os

def prompt(msg):
    response = input(msg)
    if response.lower() in ["exit", "quit"]:
        print("Exiting without saving.")
        exit()
    return response

FILE = "Financial_Exit_Plan_v1.xlsx"

# Check if file exists
if os.path.exists(FILE):
    df = pd.read_excel(FILE)
else:
    # Initialize file if it doesn't exist
    columns = [
        "Date", "Lane", "Action/Task", "Platform/Contact",
        "Estimated Earnings (€)", "Time Investment", "Status", "Notes"
    ]
    df = pd.DataFrame(columns=columns)

# Gather task data using safe prompt
today = str(date.today())
lane = prompt("Lane (e.g. Lane 1 - Immediate Cash Flow): ")
task = prompt("Action/Task: ")
platform = prompt("Platform/Contact: ")
earnings = prompt("Estimated Earnings (€): ")
time_cost = prompt("Time Investment (Low/Medium/High): ")
status = prompt("Status (Planned/In Progress/Done): ")
notes = prompt("Notes: ")

# Append the new row
new_row = {
    "Date": today,
    "Lane": lane,
    "Action/Task": task,
    "Platform/Contact": platform,
    "Estimated Earnings (€)": earnings,
    "Time Investment": time_cost,
    "Status": status,
    "Notes": notes
}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)

# Save the updated file
df.to_excel(FILE, index=False)
print(f"\n✅ Task logged successfully to {FILE}")

