---
jupyter:
  jupytext:
    text_representation:
      extension: .md
      format_name: markdown
      format_version: '1.3'
      jupytext_version: 1.16.2
  kernelspec:
    display_name: Python 3
    language: python
    name: python3
---

# Patch Tuesday - Data Cleaning

```python
import json

import pandas as pd
```

## Integrating MSRC, CISA KEV, and EPSS Data

This section of the notebook focuses on consolidating vulnerability data from multiple sources to provide a comprehensive view of security threats and their exploitability. The integration process combines data from [Microsoft Security Response Center (MSRC)](https://msrc.microsoft.com/update-guide/), [CISA's Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog), and the [Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss). 

The following steps describe how the data is processed:

1. **Load MSRC Data**: The JSON file containing MSRC vulnerability data is loaded from the local storage. This data includes detailed information about vulnerabilities that have been identified in Microsoft products.

2. **Load CISA KEV and EPSS Data**: We also load the CISA KEV data and EPSS scores from CSV files. The CISA KEV data provides information about vulnerabilities known to be exploited, and EPSS offers a probabilistic score indicating the likelihood of a vulnerability being exploited.

3. **Data Mapping and Processing**:
   - **CVE Identification**: Extract the CVE (Common Vulnerabilities and Exposures) identifiers from the MSRC data.
   - **CVSS Scores**: Gather all CVSS (Common Vulnerability Scoring System) scores provided for each vulnerability and determine the maximum score to gauge the severity.
   - **CISA and EPSS Integration**: Check if each CVE from MSRC is listed in the CISA KEV and retrieve the corresponding EPSS score if available.
   - **Threat Categorization**: Using a predefined mapping, categorize each threat associated with a vulnerability based on its type (Impact, Severity, Exploit Status).

4. **Compile Combined Data**:
   - An integrated list is compiled for each vulnerability, including its CVE identifier, title, maximum CVSS score, presence in CISA KEV, EPSS score, product details, and threat categorization.

5. **Create a DataFrame**: The collected data is structured into a pandas DataFrame. This DataFrame serves as a structured repository of combined data that can be easily analyzed and manipulated.

6. **Save the Processed Data**: Finally, the DataFrame is saved to a CSV file in the `processed` directory, making it accessible for further analysis or reporting.

This integrated approach not only enhances our ability to analyze the data effectively but also supports more informed decision-making regarding vulnerability management and response strategies.

```python
# Load the MSRC JSON data
with open('../../data/patch_tuesday/raw/msrc.json', 'r') as file:
    msrc_json = json.load(file)

# Load CSV data for CISA KEV and EPSS
cisa_kev_msrc = pd.read_csv('../../data/patch_tuesday/raw/cisa_kev.csv')
epss = pd.read_csv('../../data/patch_tuesday/raw/epss.csv')

msrc_kev_epss_data = []

threat_type_mapping = {
    0: 'Impact',
    3: 'Severity',
    1: 'Exploit Status'
}

vulnerabilities = msrc_json.get('Vulnerability', [])

for vulnerability in vulnerabilities:
    cve = vulnerability.get("CVE", "")
    title = vulnerability.get("Title").get("Value", "")
    cvss_scores = [cvss.get("BaseScore", "") for cvss in vulnerability.get("CVSSScoreSets", [])]
    if cvss_scores:
        cvss_score = max(cvss_scores)
    else:
        cvss_score = None
    cisa_kev = cve in cisa_kev_msrc["cveID"].values

    epss_score = epss.loc[epss['cve'] == cve, 'epss'].values[0] if cve in epss['cve'].values else None

    threats = {}
    for threat in vulnerability.get("Threats", []):
        threat_type = threat_type_mapping.get(threat.get("Type", 0), "")
        threat_value = threat.get("Description").get("Value", "")
        threats.update({threat_type: threat_value})

    impact = threats.get('Impact', "")
    severity = threats.get('Severity', "")
    exploit_status = threats.get('Exploit Status', "")

    product = next((note.get("Value", "") for note in vulnerability.get("Notes", []) if note.get("Type") == 7), "")

    msrc_kev_epss_data.append([cve, title, cvss_score, cisa_kev, epss_score, product, impact, severity, exploit_status])

# Create a DataFrame from the data
msrc_epss_kev = pd.DataFrame(msrc_kev_epss_data,
                             columns=["CVE", "Title", "Max CVSS", "CISA KEV", "EPSS", "Product", "Impact", "Severity",
                                      "Exploit Status"])

# Save to CSV
msrc_epss_kev.to_csv("../../data/patch_tuesday/processed/msrc_epss_kev.csv", index=False)
```
