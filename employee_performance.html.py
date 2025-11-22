import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import inspect

# ------------------------------------------------
# 1. CREATE SYNTHETIC DATA (100 employees)
# ------------------------------------------------
data = {
    "Employee": [f"E{i}" for i in range(1, 101)],
    "Department": ["Sales", "HR", "Engineering", "Marketing", "Finance"] * 20
}

df = pd.DataFrame(data)

# Frequency count for Sales department
sales_count = df[df["Department"] == "Sales"].shape[0]
print("Sales Frequency:", sales_count)

# ------------------------------------------------
# 2. CREATE HISTOGRAM AND ENCODE AS BASE64 PNG
# ------------------------------------------------
plt.figure(figsize=(8, 6))
sns.countplot(data=df, x="Department", palette="Set2")
plt.title("Department Distribution")
plt.xlabel("Department")
plt.ylabel("Count")

buffer = BytesIO()
plt.savefig(buffer, format="png")
buffer.seek(0)
img_base64 = base64.b64encode(buffer.read()).decode("utf-8")
plt.close()

# ------------------------------------------------
# 3. GET PYTHON CODE AS TEXT TO EMBED IN HTML
# ------------------------------------------------
code_text = inspect.getsource(inspect.getmodule(inspect.currentframe()))

# ------------------------------------------------
# 4. BUILD FINAL HTML (STATIC, NO JAVASCRIPT)
# ------------------------------------------------
html = f"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Employee Visualization</title>
</head>
<body>

<h2>Employee Performance Visualization</h2>

<p><strong>Verification Email:</strong> 24ds2000104@ds.study.iitm.ac.in</p>

<h3>Python Code Used</h3>
<pre><code>{code_text}</code></pre>

<h3>Sales Department Frequency</h3>
<p><strong>{sales_count}</strong></p>

<h3>Histogram Visualization</h3>
<img src="data:image/png;base64,{img_base64}" alt="Histogram" />

</body>
</html>
"""

# ------------------------------------------------
# 5. SAVE HTML FILE
# ------------------------------------------------
with open("employee_visualization.html", "w", encoding="utf-8") as f:
    f.write(html)

print("employee_visualization.html created successfully!")
