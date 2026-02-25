from water_analyzer import read_csv
import matplotlib.pyplot as plt

# Read data
data = read_csv("water_data.csv")

# Separate SAFE and UNSAFE counts
safe_count = sum(1 for d in data if d.status == "SAFE")
unsafe_count = sum(1 for d in data if d.status == "UNSAFE")

print("Total Water Records:", len(data))
print(f"SAFE: {safe_count} | UNSAFE: {unsafe_count}")
print("---------------------------------------")

for d in data:
    print(
        "Location:", d.location,
        "| pH:", d.ph,
        "| TDS:", d.tds,
        "| Turbidity:", d.turbidity,
        "| Temp:", d.temperature,
        "| Status:", d.status,
        "| Risk Level:", d.risk_level
    )

# -----------------------------
# Graph 1: SAFE vs UNSAFE
labels = ['SAFE', 'UNSAFE']
counts = [safe_count, unsafe_count]

plt.figure(figsize=(6,4))
plt.bar(labels, counts, color=['green','red'])
plt.title('Number of SAFE vs UNSAFE Water Samples')
plt.ylabel('Count')
plt.show()

# -----------------------------
# Graph 2: pH vs TDS scatter plot
ph_values = [d.ph for d in data]
tds_values = [d.tds for d in data]
colors = ['green' if d.status=='SAFE' else 'red' for d in data]

plt.figure(figsize=(6,4))
plt.scatter(ph_values, tds_values, c=colors)
plt.title('pH vs TDS of Water Samples')
plt.xlabel('pH')
plt.ylabel('TDS')
plt.show()

# -----------------------------
# Graph 3: Turbidity vs Temperature scatter
turbidity_values = [d.turbidity for d in data]
temperature_values = [d.temperature for d in data]

plt.figure(figsize=(6,4))
plt.scatter(temperature_values, turbidity_values, c=colors)
plt.title('Turbidity vs Temperature')
plt.xlabel('Temperature')
plt.ylabel('Turbidity')
plt.show()

# -----------------------------
# Graph 4: pH distribution histogram
plt.figure(figsize=(6,4))
plt.hist(ph_values, bins=8, color='skyblue', edgecolor='black')
plt.title('pH Distribution of Water Samples')
plt.xlabel('pH')
plt.ylabel('Number of Samples')
plt.show()

# -----------------------------
# Graph 5: TDS distribution histogram
plt.figure(figsize=(6,4))
plt.hist(tds_values, bins=8, color='orange', edgecolor='black')
plt.title('TDS Distribution of Water Samples')
plt.xlabel('TDS')
plt.ylabel('Number of Samples')
plt.show()

