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

# Patch Tuesday - Vulnerability Analysis

```python
import pandas as pd
from IPython.display import Markdown, display
```

```python
# Read CSV into a Pandas DataFrame
patch_tuesday_df = pd.read_csv("../../data/patch_tuesday/processed/patch_tuesday_prioritized.csv")


# Function to display Markdown text
def print_md(text):
    display(Markdown(text))


# Data Extraction
# Total CVEs
total_cves = patch_tuesday_df["CVE"].nunique()

# Severity Distribution
severity_counts = patch_tuesday_df["Severity"].value_counts().to_dict()

# Affected Products
total_products_affected = patch_tuesday_df["Product"].nunique()
top_affected_products = patch_tuesday_df["Product"].value_counts().head(3).to_dict()

# Top 5 Prioritized Vulnerabilities
top_5_vulnerabilities = (
    patch_tuesday_df.sort_values(by="CVSS", ascending=False)
    .head(5)[["CVE", "CVSS", "EPSS"]]
    .to_dict(orient="records")
)

# Impact
impact_factors = (
    patch_tuesday_df["Impact"].value_counts(normalize=True).mul(100).round(1).to_dict()
)

# Display Summary
print_md("# Patch Tuesday Summary\n")

print_md(
    "## Overview\nThis summary provides an overview of the key findings from the latest Patch Tuesday updates, including the total count of CVEs, severity distribution, affected products, top prioritized vulnerabilities, and impact.\n"
)

# Count of CVEs
print_md("## Count of CVEs\n")
print_md(f"- **Total CVEs**: {total_cves}\n")

# Severity Distribution
print_md("## Severity Distribution\n")
for severity, count in severity_counts.items():
    print_md(f"- **{severity}**: {count}")

# Affected Products
print_md("\n## Affected Products\n")
print_md(f"- **Total Products Affected**: {total_products_affected}\n")
print_md("- **Top Affected Products**:")
for product, count in top_affected_products.items():
    print_md(f" - {product}: {count} vulnerabilities")

# Top 5 Prioritized Vulnerabilities
print_md("\n## Top 5 Prioritized Vulnerabilities\n")
for vuln in top_5_vulnerabilities:
    print_md(
        f"1. **{vuln['CVE']}**\n   - **CVSS Score**: {vuln['CVSS']}\n   - **EPSS Score**: {vuln['EPSS']}\n"
    )

# Impact
print_md("## Impact\n")
for factor, percentage in impact_factors.items():
    print_md(f"- {factor}: {percentage}%")
```
