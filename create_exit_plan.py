import pandas as pd

# Define your columns
columns = [
    "Date", "Lane", "Action/Task", "Platform/Contact",
    "Estimated Earnings (€)", "Time Investment",
    "Status", "Notes"
]

# Define some starter rows
data = [
    ["2025-04-24", "Lane 1 - Immediate Cash Flow", "Post tutoring ad on HelloTalk", "HelloTalk", 25, "Low", "Planned", ""],
    ["2025-04-24", "Lane 2 - Mid-Term Exit Plan", "Prepare psych/data freelance profile", "Upwork", 35, "Medium", "In Progress", ""],
    ["2025-04-24", "Lane 3 - Long-Term Sovereignty", "Draft outline for Standalone_Complex_Profiler whitepaper", "Personal Site", 0, "High", "Not Started", ""]
]

# Create DataFrame and export to Excel
df = pd.DataFrame(data, columns=columns)
df.to_excel("Financial_Exit_Plan_v1.xlsx", index=False)
print("Financial_Exit_Plan_v1.xlsx has been created.")

