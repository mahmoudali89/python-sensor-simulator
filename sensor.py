import random
import time
import json

class Sensor:
    def __init__(self, sensor_id, sensor_type):
        self.sensor_id = sensor_id
        self.sensor_type = sensor_type
        self.status = "active"

    def read_value(self):
        if self.sensor_type == "temperature":
            return round(random.uniform(20, 35), 1)
        elif self.sensor_type == "humidity":
            return round(random.uniform(30, 70), 1)
        else:
            return None

    def get_status(self):
        return self.status

    def simulate_readings(self, count=5, interval=2):
        readings = []
        for i in range(count):
            value = self.read_value()
            reading = {
                "sensor_id": self.sensor_id,
                "sensor_type": self.sensor_type,
                "value": value,
                "reading_number": i + 1
            }
            readings.append(reading)
            print(f"Reading {i + 1}: {value}")
            time.sleep(interval)
        return readings


temp_sensor = Sensor(sensor_id=1, sensor_type="temperature")
data = temp_sensor.simulate_readings(count=5, interval=2)

with open("readings.json", "w") as f:
    json.dump(data, f, indent=2)

print("All readings saved to readings.json")