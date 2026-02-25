import csv
from water_data import WaterData

def read_csv(filepath):
    data_list = []

    with open(filepath, newline='') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  # skip header

        for row in reader:
            water = WaterData(
                row[0],
                float(row[1]),
                float(row[2]),
                float(row[3]),
                float(row[4])
            )
            # calculate status automatically
            if 6.5 <= water.ph <= 8.5 and water.tds <= 500 and water.turbidity <= 5:
                water.status = "SAFE"
                water.risk_level = "LOW RISK"
            else:
                water.status = "UNSAFE"
                water.risk_level = "HIGH RISK"

            data_list.append(water)

    return data_list

