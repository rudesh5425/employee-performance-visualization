# Employee Performance Visualization
# Email required for verification:
# 24ds2000104@ds.study.iitm.ac.in

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mpld3

# --------------------------------------
# Create a synthetic dataset (100 rows)
# --------------------------------------
data = {
    "Employee": [f"E{i}" for i in range(1, 101)],
    "Department": [
        "Sales", "HR", "Engineering", "Marketing", "Finance"
    ] * 20,
    "Region": [
        "North", "South", "East", "West", "Central"
    ] * 20,
    "PerformanceScore": [
        50, 70, 85, 60, 90
    ] * 20
}

df = pd.DataFrame(data)

# --------------------------------------
# Calculate frequency count for Sales
# --------------------------------------
sales_count = df[df["Department"] == "Sales"].shape[0]
print("Sales Department Frequency:", sales_count)

# --------------------------------------
# Create Histogram
# --------------------------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Department", palette="Set2")
plt.title("Department Distribution (Employee Count)")
plt.xlabel("Department")
plt.ylabel("Count")

# --------------------------------------
# Convert plot to HTML
# --------------------------------------
html_plot = mpld3.fig_to_html(plt.gcf())

# --------------------------------------
# ADD EMAIL INSIDE HTML FILE
# --------------------------------------
email_block = """
<div style="margin-top:20px; font-size:14px; color:#444;">
    Verification Email: 24ds2000104@ds.study.iitm.ac.in
</div>
"""

html_final = html_plot + email_block

# --------------------------------------
# Save HTML
# --------------------------------------
with open("employee_visualization.html", "w") as f:
    f.write(html_final)

print("HTML file created with email embedded: employee_visualization.html")
