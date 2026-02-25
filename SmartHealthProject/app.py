from flask import Flask, render_template, request
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

app = Flask(__name__)

# ===============================
# LOAD DATASET
# ===============================
data = pd.read_csv("water_data.csv")

# column safe format
data.columns = data.columns.str.strip()

print("Dataset Loaded")
print(data.columns)

# ===============================
# TRAIN ML MODEL
# ===============================
X = data[["pH", "TDS", "Turbidity", "Temperature"]]
y = data["Status"]

model = RandomForestClassifier()
model.fit(X, y)

print("Model trained successfully")

# ===============================
# GET LOCATIONS FROM CSV
# ===============================
states = sorted(data["Location"].dropna().unique().tolist())

print("Locations:", states[:10])  # debug

# ===============================
# HOME + FORM SUBMIT (SINGLE ROUTE)
# ===============================
@app.route("/", methods=["GET", "POST"])
def home():

    result = None

    if request.method == "POST":
        state = request.form["state"]

        state_data = data[data["Location"] == state]

        if not state_data.empty:
            avg = state_data[["pH","TDS","Turbidity","Temperature"]].mean()

            result = {
                "ph": round(avg["pH"],2),
                "tds": round(avg["TDS"],2),
                "turbidity": round(avg["Turbidity"],2),
                "temperature": round(avg["Temperature"],2),
                "quality": "Safe" if 6.5 <= avg["pH"] <= 8.5 and avg["TDS"] <= 500 else "Unsafe"
            }

    return render_template("index.html",
                           states=states,
                           result=result)

# ===============================
# RUN SERVER
# ===============================
if __name__ == "__main__":
    print("Starting Flask server...")
    app.run(debug=True)