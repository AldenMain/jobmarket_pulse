# Job Market Pulse – A Python Tool to Analyze my Job Search

A Python-based tool to track, analyze, and optimize my job applications using real-time feedback, rejection patterns, and cold hard data.

---

## Features

- Tracks applications, outcomes, and response times
- Visualizes trends (ghosting rate, success by industry, etc.)
- Extracts keywords from job ads to optimize my CV
- Highlights what strategies actually work (custom cover letters, LinkedIn contacts, etc.)

---

## Tech Stack

- Python
- pandas, matplotlib, seaborn
- scikit-learn for keyword extraction
- WordCloud
- Jupyter Notebook

---

## Sample Outputs

![Chart Example](link-to-screenshot-tbd-later.png)

---

## How to Use

1. Clone this repo  
2. Add my job data to `applications.csv` (sample included)  
3. Run the notebook: `job_tracker.ipynb`  
4. Update my entries over time and generate insights

---

## 📁 Folder Structure

jobmarket_pulse/
├── job_tracker.ipynb         # Main analysis notebook
├── log_application.py        # CLI logger for new job entries
├── applications.csv          # Your job data
├── README.md                 # This file
└── screenshots/              # Output charts and visuals

[yaml]

name: jobmarket_pulse
version: 1.0
dependencies:
  - pandas
  - matplotlib
  - seaborn

