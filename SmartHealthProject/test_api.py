from flask import Flask, render_template, request, jsonify
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import requests

app = Flask(__name__)

# ===============================
# LIVE WATER DATA FUNCTION
# ===============================
def fetch_live_water_data():

    url = "https://waterservices.usgs.gov/nwis/iv/?format=json&sites=01646500"

    response = requests.get(url)
    data = response.json()

    series = data["value"]["timeSeries"]

    water_data = {}

    for item in series:
        name = item["variable"]["variableName"].lower()
        value = item["values"][0]["value"][-1]["value"]

        if "ph" in name:
            water_data["ph"] = float(value)

        elif "turbidity" in name:
            water_data["turbidity"] = float(value)

        elif "temperature" in name:
            water_data["temperature"] = float(value)

        elif "oxygen" in name:
            water_data["dissolved_oxygen"] = float(value)

    return water_data


# ===============================
# TEST LIVE DATA ROUTE
# ===============================
@app.route("/live_data")
def live_data():
    data = fetch_live_water_data()
    return jsonify(data)


# ===============================
# LOAD DATASET
# ===============================
data = pd.read_csv("water_data.csv")
data.columns = data.columns.str.strip()

print("Dataset Loaded")
print("Columns:", data.columns)

# ===============================
# TRAIN ML MODEL
# ===============================
X = data[["pH", "TDS", "Turbidity", "Temperature"]]
y = data["Status"]

model = RandomForestClassifier()
model.fit(X, y)

print("Model trained successfully")

# ===============================
# GET LOCATIONS
# ===============================
states = sorted(data["Location"].dropna().unique().tolist())


# ===============================
# HOME PAGE
# ===============================
@app.route("/")
def home():
    return render_template("index.html", states=states)


# ===============================
# STATE DATA API
# ===============================
@app.route("/get_state_data", methods=["POST"])
def get_state_data():

    state = request.form["state"]
    state_data = data[data["Location"] == state]

    avg = state_data[["pH","TDS","Turbidity","Temperature"]].mean()

    return jsonify({
        "pH": float(avg["pH"]),
        "TDS": float(avg["TDS"]),
        "Turbidity": float(avg["Turbidity"]),
        "Temperature": float(avg["Temperature"]),
        "Status": "SAFE" if avg["pH"]>=6.5 and avg["pH"]<=8.5 and avg["TDS"]<=500 else "UNSAFE"
    })


# ===============================
# PARAMETER PREDICTION API
# ===============================
@app.route("/predict", methods=["POST"])
def predict():

    ph = float(request.form["ph"])
    tds = float(request.form["tds"])
    turbidity = float(request.form["turbidity"])
    temp = float(request.form["temp"])

    prediction = model.predict([[ph, tds, turbidity, temp]])[0]

    return jsonify({"status": prediction})


# ===============================
# RUN
# ===============================
if __name__ == "__main__":
    app.run(debug=True)
