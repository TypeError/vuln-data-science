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

# Patch Tuesday - Data Collection

```python
import json
import os
from datetime import datetime

import pandas as pd
import requests
```

## Project Setup

Before proceeding with data collection, we need to ensure that the necessary directories for storing raw and processed data are in place. This step is crucial to maintain an organized structure for our project, especially when working with multiple datasets over time.

The following Python code will check if the required directories exist (`raw` and `processed` under `patch_tuesday`), and if not, it will create them. This approach ensures that the environment is always correctly set up before any data processing begins, even if you're running this notebook on a new machine or a fresh clone of the repository.


```python
# Directories to create
dirs = [
    "../../data/patch_tuesday/raw/",
    "../../data/patch_tuesday/processed/",
]

# Create Patch Tuesday data directories if they don't exist
for d in dirs:
    os.makedirs(d, exist_ok=True)
```

## Fetching and Storing Microsoft Security Updates

This section of the notebook is dedicated to retrieving the latest security updates from the Microsoft Security Response Center (MSRC) API ([https://msrc.microsoft.com/update-guide/](https://msrc.microsoft.com/update-guide/)). 

The process is outlined in the following steps:

1. **Fetch Updates List**: We begin by making a GET request to the MSRC API to fetch a list of recent updates. This list contains various details, including URLs to the detailed Common Vulnerability Reporting Framework (CVRF) documents for each update.

2. **Extract Latest Update URL**: From the fetched updates, we extract the URL of the most recent CVRF document, which provides detailed information about the vulnerabilities addressed in the latest Patch Tuesday.

3. **Retrieve CVRF Details**: Using the URL obtained in the previous step, another GET request is made to download the complete CVRF document that includes detailed descriptions of each vulnerability.

4. **Parse CVE Identifiers**: We extract CVE identifiers from the CVRF document to list all the vulnerabilities covered in the latest update.

5. **Store JSON Data**: Finally, the entire CVRF JSON data is saved to a local file. This file is stored in the `../../data/raw` directory, allowing us to reference this data later for analysis without needing to re-fetch it from the API.

By automating the collection and storage of this data, we streamline the process of analyzing the latest security vulnerabilities released on Patch Tuesday, facilitating quicker and more informed security responses.

```python
# Get Microsoft security updates from MSRC API
updates = requests.get(
    "https://api.msrc.microsoft.com/cvrf/v3.0/updates",
    headers={"Accept": "application/json"},
)

sorted_updates = sorted(
    updates.json()["value"],
    key=lambda x: datetime.fromisoformat(
        x["InitialReleaseDate"].replace("Z", "+00:00")
    ),
)

latest_msrc_url = sorted_updates[-1]["CvrfUrl"]

# Get current CVRF from MSRC API
msrc_response = requests.get(latest_msrc_url, headers={"Accept": "application/json"})

msrc_json = msrc_response.json()

cves = list(set([x["CVE"] for x in msrc_json["Vulnerability"]]))

with open("../../data/patch_tuesday/raw/msrc.json", "w") as file:
    json.dump(msrc_json, file, indent=2)
```

## Fetching EPSS Scores for CVEs from MSRC Updates

This section of the notebook focuses on retrieving the Exploit Prediction Scoring System (EPSS) scores for CVEs associated with the latest Microsoft Security Response Center (MSRC) updates. 

The steps for this process are outlined below:

1. **Divide CVEs into Chunks**: Given the potential limitations on URL length or API request size, the list of CVE identifiers is split into three smaller chunks. This division ensures that we can query the API without exceeding URL length restrictions.

2. **Initialize Storage List**: A list called `epss_list` is initialized to store the data fetched in batches.

3. **Fetch EPSS Data**: For each chunk of CVEs, a URL is constructed to request their EPSS scores in CSV format from the FIRST.org API. The data from each request is read directly into a pandas DataFrame, which is then appended to the `epss_list`.

4. **Concatenate DataFrames**: After all chunks are processed, the individual DataFrames stored in `epss_list` are concatenated into a single DataFrame. This consolidated DataFrame, `epss`, contains all the EPSS scores for the CVEs.

5. **Save Data to CSV**: The final DataFrame is saved to a CSV file in the `../../data/raw/` directory. This approach ensures that the EPSS data is easily accessible for further analysis and does not require re-fetching from the API.

By automating the retrieval and storage of EPSS data, we enhance our ability to quickly analyze the exploitability of newly reported vulnerabilities and prioritize responses accordingly.

See EPSS at [https://www.first.org/epss](https://www.first.org/epss).

```python
# Get latest EPSS data from First.org for MSRC CVEs
cve_chunk_size = 100
cve_chunks = [cves[i: i + cve_chunk_size] for i in range(0, len(cves), cve_chunk_size)]

epss_list = []

for chunk in cve_chunks:
    epss_url = f"https://api.first.org/data/v1/epss.csv?cve={','.join(chunk)}"
    epss_data = pd.read_csv(epss_url)
    epss_list.append(epss_data)

epss = pd.concat(epss_list)

# Save to CSV
epss.to_csv("../../data/patch_tuesday/raw/epss.csv", index=False)
```




## Retrieving and Processing CISA Known Exploited Vulnerabilities Data

This section of the notebook is dedicated to acquiring and refining the data from CISA's Known Exploited Vulnerabilities (KEV) ([https://www.cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog)) repository. 

The code performs the following operations:

1. **Fetch KEV Data**: We begin by downloading the latest KEV data directly from CISA's official website. This dataset is publicly available and is regularly updated to reflect the most current list of vulnerabilities known to be exploited.

2. **Filter for MSRC CVEs**: The fetched data is then filtered to retain only those CVEs (Common Vulnerabilities and Exposures) that are relevant to our previously fetched MSRC (Microsoft Security Response Center) CVE list. This step ensures that our analysis focuses only on vulnerabilities that intersect with Microsoft's updates.

3. **Save Filtered Data**: The filtered dataset is saved to a CSV file in the `../../data/raw/` directory. Storing this data locally allows us to access and analyze it more efficiently in subsequent steps without repeated downloads.

By integrating CISA's KEV data into our analysis, we enhance our understanding of the security landscape, particularly regarding vulnerabilities that have been actively exploited in the wild. This information is crucial for prioritizing patches and mitigating risks associated with known threats.

```python
# Get CISA KEV (Known Exploited Vulnerabilities) data
cisa_kev = pd.read_csv(
    "https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv"
)

# Filter CISA KEV data for MSRC CVEs
cisa_kev_msrc = cisa_kev[cisa_kev["cveID"].isin(cves)]

# Save to CSV
cisa_kev_msrc.to_csv("../../data/patch_tuesday/raw/cisa_kev.csv", index=False)
```
