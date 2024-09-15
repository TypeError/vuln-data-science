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

# Weekly CVE - Vulnerability Summary

```python
import pandas as pd
from IPython.display import Markdown, display
```

```python
## Read CSV into a Pandas DataFrame

```

```python
weekly_cve_df = pd.read_csv("../../data/weekly_cve/processed/nvd_epss_kev.csv")
```

## Display Summary

```python
# Function to display Markdown text
def print_md(text):
    display(Markdown(text))


# Data Extraction

# Total CVEs
total_cves = weekly_cve_df["CVE"].nunique()

# Severity Distribution
severity_counts = weekly_cve_df["CVSS_Severity"].value_counts()

# Vulnerability Status Distribution
status_counts = weekly_cve_df["Vuln_Status"].value_counts()

# Affected Vendors
total_vendors_affected = weekly_cve_df["Vendor"].nunique()
top_affected_vendors = weekly_cve_df["Vendor"].value_counts().head(3)

# Top 10 Prioritized Vulnerabilities
top_10_vulnerabilities = (
    weekly_cve_df.sort_values(by=["CVSS_Base_Score", "EPSS"], ascending=[False, False])
    .head(10)[
        [
            "CVE",
            "CVSS_Base_Score",
            "EPSS",
            "Vendor",
            "Product",
            "Description",
            "CISA_KEV",
            "Vuln_Status",
        ]
    ]
    .to_dict(orient="records")
)

# Calculate percentages
severity_percentages = (severity_counts / total_cves) * 100
status_percentages = (status_counts / total_cves) * 100
vendor_percentages = (top_affected_vendors / total_vendors_affected) * 100

# Display Summary

# Title and Overview
print_md("# Weekly Cybersecurity Vulnerability Report\n")
print_md(
    "## Overview\nThis summary provides an overview of the key critical and high-severity vulnerabilities reported in the past week.\n"
)

# Count of CVEs
print_md(f"**Total CVEs Reported**: {total_cves}\n")

# Severity Distribution
print_md("### Severity Distribution\n")
for severity, count in severity_counts.items():
    percentage = severity_percentages[severity]
    print_md(f"- **{severity.title()}**: {count} ({percentage:.0f}%)")

# Vulnerability Status Distribution
print_md("\n### Vulnerability Status Distribution\n")
for status, count in status_counts.items():
    percentage = status_percentages[status]
    print_md(f"- **{status}**: {count} ({percentage:.0f}%)")

# Affected Vendors
print_md("\n## Affected Vendors\n")
print_md(f"- **Total Vendors Affected**: {total_vendors_affected}\n")
print_md("### Top Affected Vendors:")
for vendor, count in top_affected_vendors.items():
    percentage = vendor_percentages[vendor]
    print_md(f"- **{vendor.title()}**: {count} vulnerabilities ({percentage:.0f}%)")

# Notable Vulnerabilities
print_md("\n## Notable Vulnerabilities\n")
for idx, vuln in enumerate(top_10_vulnerabilities, 1):
    print_md(f"### {idx}. {vuln['CVE']}\n")
    if pd.notna(vuln['Vendor']):
        print_md(f"- **Affected Product**: {vuln['Vendor'].title()} {vuln['Product'].title()}\n")
    print_md(f"- **Description**: {vuln['Description'].replace('\n', ' ')}\n")
    print_md(f"- **CVSS Base Score**: {vuln['CVSS_Base_Score']}\n")
    print_md(f"- **EPSS Score**: {vuln['EPSS']}\n")
    print_md(f"- **CISA KEV**: {'Yes' if vuln['CISA_KEV'] else 'No'}\n")
    print_md(f"- **Vulnerability Status**: {vuln['Vuln_Status']}\n")
```
