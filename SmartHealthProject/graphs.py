import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
data = pd.read_csv("water_data.csv")

# -------- GRAPH 1: pH Distribution ----------
plt.figure(figsize=(6,4))
plt.hist(data['pH'], bins=10, color='skyblue', edgecolor='black')
plt.title("pH Value Distribution")
plt.xlabel("pH")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# -------- GRAPH 2: TDS Distribution ----------
plt.figure(figsize=(6,4))
plt.hist(data['TDS'], bins=10, color='orange', edgecolor='black')
plt.title("TDS Distribution")
plt.xlabel("TDS (ppm)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# -------- GRAPH 3: Turbidity Distribution ----------
plt.figure(figsize=(6,4))
plt.hist(data['Turbidity'], bins=10, color='green', edgecolor='black')
plt.title("Turbidity Distribution")
plt.xlabel("Turbidity")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# -------- GRAPH 4: Temperature Distribution ----------
plt.figure(figsize=(6,4))
plt.hist(data['Temperature'], bins=10, color='red', edgecolor='black')
plt.title("Temperature Distribution")
plt.xlabel("Temperature (°C)")
plt.ylabel("Frequency")
plt.grid(True)
plt.show()

# -------- GRAPH 5: SAFE vs UNSAFE Count ----------
status_counts = data['Status'].value_counts()

plt.figure(figsize=(6,4))
plt.bar(status_counts.index, status_counts.values, color=['green','red'], edgecolor='black')
plt.title("Water Quality Status Count")
plt.xlabel("Status")
plt.ylabel("Number of Samples")
plt.grid(axis='y')
plt.show()
