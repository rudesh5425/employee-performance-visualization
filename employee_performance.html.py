# create_html.py
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import mpld3
import inspect
import sys   # FIXED: required for inspect.getsource()

# -------------------------------
# 1. CREATE DATASET
# -------------------------------
data = {
    "Employee": [f"E{i}" for i in range(1, 101)],
    "Department": ["Sales", "HR", "Engineering", "Marketing", "Finance"] * 20
}

df = pd.DataFrame(data)

# Frequency count for Sales
sales_count = df[df["Department"] == "Sales"].shape[0]

# -------------------------------
# 2. CREATE VISUALIZATION
# -------------------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Department", palette="Set2")
plt.title("Department Distribution (Employee Count)")
plt.xlabel("Department")
plt.ylabel("Count")

# Convert plot to interactive HTML
plot_html = mpld3.fig_to_html(plt.gcf())
plt.close()

# -------------------------------
# 3. READ THIS SCRIPT'S CODE AS TEXT (for embedding)
# -------------------------------
code_text = inspect.getsource(sys.modules[__name__])

# -------------------------------
# 4. BUILD FINAL HTML
# -------------------------------
html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Employee Visualization</title>
<script src="https://mpld3.github.io/js/d3.v5.min.js"></script>
<script src="https://mpld3.github.io/js/mpld3.v0.5.12.js"></script>
</head>
<body>

<h2>Employee Performance Visualization</h2>
<p><strong>Verification Email:</strong> 24ds2000104@ds.study.iitm.ac.in</p>

<h3>Python Code Used</h3>
<pre><code>{code_text}</code></pre>

<h3>Sales Department Frequency</h3>
<p><strong>{sales_count}</strong></p>

<h3>Visualization</h3>
{plot_html}

</body>
</html>
"""

# -------------------------------
# 5. SAVE FILE
# -------------------------------
with open("employee_visualization.html", "w", encoding="utf-8") as f:
    f.write(html)

print("employee_visualization.html created successfully!")
