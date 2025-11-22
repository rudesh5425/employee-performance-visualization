# save as create_combined_html.py and run: python create_combined_html.py
import pandas as pd, seaborn as sns, matplotlib.pyplot as plt, mpld3, inspect, pathlib

# --- create data & plot ---
data = {"Employee":[f"E{i}" for i in range(1,101)],
        "Department":["Sales","HR","Engineering","Marketing","Finance"]*20}
df = pd.DataFrame(data)
sales_count = df[df["Department"]=="Sales"].shape[0]

plt.figure(figsize=(8,6))
sns.countplot(data=df, x="Department", palette="Set2")
plt.title("Department Distribution (Employee Count)")
plt.xlabel("Department")
plt.ylabel("Count")
plot_html = mpld3.fig_to_html(plt.gcf())
plt.close()

# --- read this file's source to embed (or supply your script file path) ---
this_file = pathlib.Path(__file__).name
with open(this_file, "r", encoding="utf-8") as f:
    code_text = f.read()

# --- build combined html ---
html = f"""<!doctype html>
<html><head><meta charset="utf-8"><title>Employee Visualization</title></head><body>
<h2>Employee Performance Visualization</h2>
<p>Verification Email: 24ds2000104@ds.study.iitm.ac.in</p>
<h3>Python code used</h3><pre><code>{code_text}</code></pre>
<h3>Sales Department Frequency</h3><p>{sales_count}</p>
<h3>Visualization</h3>{plot_html}
</body></html>"""

with open("employee_visualization.html","w",encoding="utf-8") as f:
    f.write(html)
print("Created employee_visualization.html with embedded code, plot and email.")
