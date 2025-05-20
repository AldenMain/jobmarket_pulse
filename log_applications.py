#!/usr/bin/env python
# coding: utf-8

# ## log_applications

# In[ ]:


import csv
from datetime import datetime

def log_new_application():
    fields = [
        "Job_Title", "Company", "Industry", "Application_Date", "Response_Date",
        "Outcome", "CV_Version", "Cover_Letter_Customized",
        "LinkedIn_Connection", "Location", "Salary_Range", "Job_Description"
    ]

    data = {
        "Job_Title": input("Job Title: "),
        "Company": input("Company: "),
        "Industry": input("Industry: "),
        "Application_Date": datetime.today().strftime("%Y-%m-%d"),
        "Response_Date": "",
        "Outcome": "",
        "CV_Version": input("CV Version used (e.g. v1, v2): "),
        "Cover_Letter_Customized": input("Custom Cover Letter? (Yes/No): "),
        "LinkedIn_Connection": input("Messaged anyone on LinkedIn? (Yes/No): "),
        "Location": input("Job Location: "),
        "Salary_Range": input("Salary Range (if any): "),
        "Job_Description": input("Copy/paste job description (optional): ")
    }

    with open("applications.csv", "a", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        if f.tell() == 0:
            writer.writeheader()
        writer.writerow(data)

    print("Logged.")

if __name__ == "__main__":
    log_new_application()


# In[7]:


import pandas as pd

df = pd.read_csv("applications.csv", parse_dates=["Application_Date", "Response_Date"])
df.head()

