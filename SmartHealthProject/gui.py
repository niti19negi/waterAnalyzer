import tkinter as tk
from tkinter import messagebox
from water_analyzer import read_csv
from water_data import WaterData
import matplotlib.pyplot as plt

# Load dataset
data = read_csv("water_data.csv")

# -------------------
# Function to analyze single water input
def analyze_input():
    try:
        ph = float(ph_entry.get())
        tds = float(tds_entry.get())
        turbidity = float(turbidity_entry.get())
        temp = float(temp_entry.get())

        # Rule-based analysis
        if 6.5 <= ph <= 8.5 and tds <= 500 and turbidity <= 5:
            status = "SAFE"
            risk = "LOW RISK"
        else:
            status = "UNSAFE"
            risk = "HIGH RISK"

        messagebox.showinfo("Water Analysis Result",
                            f"Status: {status}\nRisk Level: {risk}")

    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers")

# -------------------
# Function to show all graphs
def show_graphs():
    # Graph 1: SAFE vs UNSAFE
    safe_count = sum(1 for d in data if d.status == "SAFE")
    unsafe_count = sum(1 for d in data if d.status == "UNSAFE")
    plt.figure(figsize=(6,4))
    plt.bar(['SAFE','UNSAFE'], [safe_count, unsafe_count], color=['green','red'])
    plt.title('Number of SAFE vs UNSAFE Water Samples')
    plt.ylabel('Count')
    plt.show()

    # Graph 2: pH vs TDS scatter
    ph_values = [d.ph for d in data]
    tds_values = [d.tds for d in data]
    colors = ['green' if d.status=='SAFE' else 'red' for d in data]
    plt.figure(figsize=(6,4))
    plt.scatter(ph_values, tds_values, c=colors)
    plt.title('pH vs TDS of Water Samples')
    plt.xlabel('pH')
    plt.ylabel('TDS')
    plt.show()

    # Graph 3: Turbidity vs Temperature scatter
    turbidity_values = [d.turbidity for d in data]
    temp_values = [d.temperature for d in data]
    plt.figure(figsize=(6,4))
    plt.scatter(temp_values, turbidity_values, c=colors)
    plt.title('Turbidity vs Temperature')
    plt.xlabel('Temperature')
    plt.ylabel('Turbidity')
    plt.show()

    # Graph 4: pH Distribution
    plt.figure(figsize=(6,4))
    plt.hist(ph_values, bins=8, color='skyblue', edgecolor='black')
    plt.title('pH Distribution')
    plt.xlabel('pH')
    plt.ylabel('Number of Samples')
    plt.show()

    # Graph 5: TDS Distribution
    plt.figure(figsize=(6,4))
    plt.hist(tds_values, bins=8, color='orange', edgecolor='black')
    plt.title('TDS Distribution')
    plt.xlabel('TDS')
    plt.ylabel('Number of Samples')
    plt.show()

# -------------------
# GUI Setup
root = tk.Tk()
root.title("Smart Water Analyzer")

# Labels & entries
tk.Label(root, text="pH:").grid(row=0, column=0)
ph_entry = tk.Entry(root)
ph_entry.grid(row=0, column=1)

tk.Label(root, text="TDS:").grid(row=1, column=0)
tds_entry = tk.Entry(root)
tds_entry.grid(row=1, column=1)

tk.Label(root, text="Turbidity:").grid(row=2, column=0)
turbidity_entry = tk.Entry(root)
turbidity_entry.grid(row=2, column=1)

tk.Label(root, text="Temperature:").grid(row=3, column=0)
temp_entry = tk.Entry(root)
temp_entry.grid(row=3, column=1)

# Buttons
tk.Button(root, text="Analyze Water", command=analyze_input, bg='lightgreen').grid(row=4, column=0, columnspan=2, sticky="we")
tk.Button(root, text="Show Graphs", command=show_graphs, bg='lightblue').grid(row=5, column=0, columnspan=2, sticky="we")

# Run GUI
root.mainloop()
