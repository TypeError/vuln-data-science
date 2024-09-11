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

# Weekly CVE - Data Cleaning

```python
import json

import pandas as pd
```

## Integrating NIST NVD and EPSS Data

This script processes data from the [NIST National Vulnerability Database (NVD)](https://nvd.nist.gov), merges it with the [Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss) dataset, and outputs a consolidated CSV file with the following key information for each vulnerability:
- **CVE ID**: The unique identifier of the vulnerability.
- **Description**: The English description of the vulnerability.
- **CVSS Base Score & Severity**: The NIST CVSS v4.0 or v3.1 base score and severity, prioritizing metrics from NIST (`nvd@nist.gov`).
- **CWE**: The primary weakness, sourced from NIST.
- **Vendor & Product**: The vendor and product associated with the vulnerability (from CPE data).
- **CISA KEV Status**: Indicates whether the vulnerability is flagged by CISA's Known Exploited Vulnerabilities (KEV) catalog.
- **EPSS Score**: The EPSS score estimating the likelihood of exploitation.
- **Vulnerability Status**: The status of the vulnerability (e.g., "Awaiting Analysis").

The final data is saved to a CSV file for further analysis.


```python
# Load the NIST NVD JSON data
with open('../../data/weekly_cve/raw/nist_nvd.json', 'r') as file:
    nvd_json = json.load(file)

# Load CSV data for CISA KEV and EPSS
cisa_kev_msrc = pd.read_csv('../../data/weekly_cve/raw/cisa_kev.csv')
epss = pd.read_csv('../../data/weekly_cve/raw/epss.csv')

# Create a dictionary for quick EPSS score lookup
epss_dict = epss.set_index('cve')['epss'].to_dict()

nvd_kev_epss_data = []

for vulnerability in nvd_json:
    cve_id = vulnerability['cve']['id']
    description = next((desc['value'] for desc in vulnerability['cve']['descriptions'] if desc['lang'] == 'en'), '')

    cve_metrics = vulnerability['cve']['metrics']
    cve_metric = next(
        (metric for metric in cve_metrics.get('cvssMetricV40', []) if metric['source'] == 'nvd@nist.gov'),
        next((metric for metric in cve_metrics.get('cvssMetricV31', []) if metric['source'] == 'nvd@nist.gov'), None)
    )

    cvss_base_score = cve_metric['cvssData']['baseScore'] if cve_metric else None
    cvss_severity = cve_metric['cvssData']['baseSeverity'] if cve_metric else None

    vendor, product = None, None
    if 'configurations' in vulnerability['cve']:
        for config in vulnerability['cve']['configurations']:
            for node in config['nodes']:
                for cpe_match in node['cpeMatch']:
                    if cpe_match['vulnerable']:
                        cpe_parts = cpe_match['criteria'].split(':')
                        vendor, product = cpe_parts[3], cpe_parts[4]
                        break

    primary_weakness = next(
        (weakness['description'][0]['value'] for weakness in vulnerability['cve']['weaknesses']
         if weakness['source'] == 'nvd@nist.gov' and weakness['type'] == 'Primary'), None
    )

    cisa_kev = 'cisaExploitAdd' in vulnerability['cve']
    vuln_status = vulnerability['cve'].get('vulnStatus')
    epss_score = epss_dict.get(cve_id)

    nvd_kev_epss_data.append([
        cve_id, description, cvss_base_score, cvss_severity, primary_weakness,
        vendor, product, cisa_kev, epss_score, vuln_status
    ])

# Define the columns and create a DataFrame
columns = [
    'CVE', 'Description', 'CVSS_Base_Score', 'CVSS_Severity', 'CWE',
    'Vendor', 'Product', 'CISA_KEV', 'EPSS', 'Vuln_Status'
]

nvd_epss_kev = pd.DataFrame(nvd_kev_epss_data, columns=columns)
nvd_epss_kev.to_csv('../../data/weekly_cve/processed/nvd_epss_kev.csv', index=False)
```
