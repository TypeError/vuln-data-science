---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.3
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Weekly CVE - Data Collection

```python
import json
import os
from datetime import datetime, timedelta

import pandas as pd
import requests
```

## Project Setup

Before proceeding with data collection, we need to ensure that the necessary directories for storing raw and processed data are in place. This step is crucial to maintain an organized structure for our project, especially when working with multiple datasets over time.

The following Python code will check if the required directories exist (`raw` and `processed` under `weekly_cve`), and if not, it will create them. This approach ensures that the environment is always correctly set up before any data processing begins, even if you're running this notebook on a new machine or a fresh clone of the repository.


```python
# Directories to create
dirs = [
    "../../data/weekly_cve/raw/",
    "../../data/weekly_cve/processed/",
]

# Create Weekly CVE data directories if they don't exist
for d in dirs:
    os.makedirs(d, exist_ok=True)
```

## Fetching and Storing Weekly CVE Data from NIST NVD API

In this cell, we are:

1. **Fetching CVE Data**:
   - We are pulling the Critical and High severity vulnerabilities published in the last week from the NIST National Vulnerability Database (NVD) using their public API.
   - We are using a helper function `fetch_nvd_vulnerabilities()` to retrieve the data based on severity (Critical or High) for a specified date range (from last week to today).

2. **Combining and Deduplicating Results**:
   - The vulnerabilities from both severity levels are combined.
   - We extract the unique CVE IDs from the combined list to ensure no duplicates.

3. **Writing the Data to a JSON File**:
   - The retrieved vulnerabilities are saved to a file in JSON format at the path `../../data/weekly_cve/raw/nist_nvd_json.json`.
   - The `json.dump()` function is used to format the data with an indentation level of 2 for readability.

This will allow us to persist the raw data locally for future analysis or record-keeping.


```python
# Function to get NVD vulnerabilities for a given severity
def fetch_nvd_vulnerabilities(severity, start_date, end_date):
    url = f"https://services.nvd.nist.gov/rest/json/cves/2.0/?pubStartDate={start_date}&pubEndDate={end_date}&cvssV3Severity={severity}"
    try:
        response = requests.get(url, headers={"Accept": "application/json"})
        response.raise_for_status()  # Raise an exception for HTTP errors
        return response.json().get("vulnerabilities", [])
    except requests.RequestException as ex:
        print(f"Error fetching {severity} vulnerabilities: {ex}")
        return []


# Get today's date and last week's date
today = datetime.today()
last_week = today - timedelta(weeks=1)

# Convert dates to string format required for NIST NVD API
date_format = '%Y-%m-%dT00:00:00.000'
today_str = today.strftime(date_format)
last_week_str = last_week.strftime(date_format)

# Fetch vulnerabilities for both Critical and High severities
vulnerabilities_critical = fetch_nvd_vulnerabilities("CRITICAL", last_week_str, today_str)
vulnerabilities_high = fetch_nvd_vulnerabilities("HIGH", last_week_str, today_str)

# Combine and deduplicate vulnerabilities based on CVE ID
vulnerabilities = vulnerabilities_critical + vulnerabilities_high
cves = list({vuln.get("cve", {}).get("id") for vuln in vulnerabilities})

# Output the number of unique CVEs found
print(f"Number of unique CVEs: {len(cves)}")

with open("../../data/weekly_cve/raw/nist_nvd.json", "w") as file:
    json.dump(vulnerabilities, file, indent=2)
```

## Fetching EPSS Scores for CVEs from NIST NVD Data

This section of the notebook focuses on retrieving the Exploit Prediction Scoring System (EPSS) scores for CVEs associated with the latest NIST NVD data.

The steps for this process are outlined below:

1. **Divide CVEs into Chunks**: Given the potential limitations on URL length or API request size, the list of CVE identifiers is split into three smaller chunks. This division ensures that we can query the API without exceeding URL length restrictions.

2. **Initialize Storage List**: A list called `epss_list` is initialized to store the data fetched in batches.

3. **Fetch EPSS Data**: For each chunk of CVEs, a URL is constructed to request their EPSS scores in CSV format from the FIRST.org API. The data from each request is read directly into a pandas DataFrame, which is then appended to the `epss_list`.

4. **Concatenate DataFrames**: After all chunks are processed, the individual DataFrames stored in `epss_list` are concatenated into a single DataFrame. This consolidated DataFrame, `epss`, contains all the EPSS scores for the CVEs.

5. **Save Data to CSV**: The final DataFrame is saved to a CSV file in the `../../data/raw/` directory. This approach ensures that the EPSS data is easily accessible for further analysis and does not require re-fetching from the API.

By automating the retrieval and storage of EPSS data, we enhance our ability to quickly analyze the exploitability of newly reported vulnerabilities and prioritize responses accordingly.

See EPSS at [https://www.first.org/epss](https://www.first.org/epss).

```python
# Get latest EPSS data from First.org for NIST NVD CVEs
cve_chunk = len(cves) // 3
cve_chunks = [cves[i: i + cve_chunk] for i in range(0, len(cves), cve_chunk)]

epss_list = []

for chunk in cve_chunks:
    epss_url = f"https://api.first.org/data/v1/epss.csv?cve={','.join(chunk)}"
    try:
        epss_data = pd.read_csv(epss_url)
        epss_list.append(epss_data)
    except Exception as e:
        print(f"Error fetching EPSS data for chunk: {chunk} - {e}")

epss = pd.concat(epss_list, ignore_index=True)

# Save to CSV
epss.to_csv('../../data/weekly_cve/raw/epss.csv', index=False)
```
