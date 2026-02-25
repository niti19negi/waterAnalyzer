import requests
import random

API_KEY = "4fdda7631a4921c30342fe7425e56d23"

def get_real_time_water_data(city="Delhi"):

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"

    response = requests.get(url)
    data = response.json()

    if "main" not in data:
        return None

    # Weather temp → water temp assume
    temperature = data["main"]["temp"]

    # Simulated water parameters
    water_data = {
        "pH": round(random.uniform(6.0, 9.0), 2),
        "TDS": random.randint(200, 800),
        "Turbidity": round(random.uniform(1, 10), 2),
        "Temperature": temperature
    }

    return water_data