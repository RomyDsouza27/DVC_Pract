import os
import pandas as pd
os.makedirs("data", exist_ok=True)
df = pd.DataFrame({
"ID": [1, 2, 3],
"Name": ["Amit", "Rahul", "Priya"],
"Marks": [85, 90, 88]
})
df.to_csv("data/students.csv", index=False)
print("CSV file created successfully.")
