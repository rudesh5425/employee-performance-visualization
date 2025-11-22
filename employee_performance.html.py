# Email for verification:
# 24ds2000104@ds.study.iitm.ac.in

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mpld3
import inspect

# ----------------------------
# CREATE SYNTHETIC DATA
# ----------------------------
data = {
    "Employee": [f"E{i}" for i in range(1, 101)],
    "Department": ["Sales", "HR", "Engineering", "Marketing", "Finance"] * 20,
    "Region": ["North", "South", "East", "West", "Central"] * 20,
    "PerformanceScore": [50, 70, 85, 60, 90] * 20
}

df = pd.DataFrame(data)

# ----------------------------
# COUNT THE SALES DEPARTMENT
# ----------------------------
sales_count = df[df["Department"] == "Sales"].shape[0]
print("Sales Department Frequency:", sales_count)

# ----------------------------
# BUILD HISTOGRAM
# ----------------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Department", palette="Set2")
plt.title("Department Distribution (Employee Count)")
plt.xlabel("Department")
plt.ylabel("Count")

# Convert plot to HTML
plot_html = mpld3.fig_to_html(plt.gcf())

# ----------------------------
# EXTRACT THIS PYTHON SCRIPT AS TEXT
# ----------------------------
with open(__file__, "r") as f:
    python_code = f.read()

# ----------------------------
# BUILD FINAL HTML
# ----------------------------
html_content = f"""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Employee Performance Visualization</title>
</head>
<body>

<h2>Employee Performance Visualization</h2>

<h3>Verification Email</h3>
<p>24ds2000104@ds.study.iitm.ac.in</p>

<h3>Python Code Used</h3>
<pre><code>
{python_code}
</code></pre>

<h3>Sales Department Frequency</h3>
<p>{sales_count}</p>

<h3>Histogram Visualization</h3>
{plot_html}

</body>
</html>
"""

# ----------------------------
# SAVE HTML FILE
# ----------------------------
with open("employee_visualization.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("employee_visualization.html has been created successfully!")
