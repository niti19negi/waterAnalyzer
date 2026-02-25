class WaterData:
    def __init__(self, location, ph, tds, turbidity, temperature):
        self.location = location
        self.ph = ph
        self.tds = tds
        self.turbidity = turbidity
        self.temperature = temperature
        self.status = ""      # will calculate later
        self.risk_level = ""  # optional: LOW / HIGH
