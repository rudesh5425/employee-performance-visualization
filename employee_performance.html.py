import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import inspect
import sys

# -------------------------------
# 1. CREATE SYNTHETIC DATA
# -------------------------------
data = {
    "Employee": [f"E{i}" for i in range(1, 101)],
    "Department": ["Sales", "HR", "Engineering", "Marketing", "Finance"] * 20
}

df = pd.DataFrame(data)

# Count frequency of Sales department
sales_count = df[df["Department"] == "Sales"].shape[0]

# -------------------------------
# 2. CREATE HISTOGRAM AND SAVE TO BASE64
# -------------------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Department", palette="Set2")
plt.title("Department Distribution (Employee Count)")
plt.xlabel("Department")
plt.ylabel("Count")

buffer = BytesIO()
plt.savefig(buffer, format="png")
buffer.seek(0)
img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
plt.close()

# -------------------------------
# 3. READ THIS SCRIPT AS TEXT
# -------------------------------
code_text = inspect.getsource(sys.modules[__name__])

# -------------------------------
# 4. BUILD HTML WITHOUT JAVASCRIPT
# -------------------------------
html = f"""
<!doctype html>
<html>
<head>
<meta charset="utf-8">
<title>Employee Visualization</title>
</head>
<body>

<h2>Employee Performance Visualization</h2>
<p><strong>Verification Email:</strong> 24ds2000104@ds.study.iitm.ac.in</p>

<h3>Python Code Used</h3>
<pre><code>{code_text}</code></pre>

<h3>Sales Department Frequency</h3>
<p><strong>{sales_count}</strong></p>

<h3>Visualization</h3>
<img src="data:image/png;base64,{img_base64}" alt="Histogram" />

</body>
</html>
"""

# -------------------------------
# 5. SAVE HTML
# -------------------------------
with open("employee_visualization.html", "w", encoding="utf-8") as f:
    f.write(html)

print("employee_visualization.html created successfully with embedded PNG chart!")
