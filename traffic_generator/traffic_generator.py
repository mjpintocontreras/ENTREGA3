# traffic_generator.py

import random
import time
import json
from bson import json_util
from pymongo import MongoClient

# Conexión a MongoDB dentro de Docker
client = MongoClient("mongodb://mongodb:27017/")
db = client["waze"]
colec = db["eventos"]

def load_events():
    return list(colec.find())

def poisson_rate(events, rate_per_sec):
    while True:
        wait = random.expovariate(rate_per_sec)
        time.sleep(wait)
        yield random.choice(events)

def uniform_rate(events, rate_per_sec):
    interval = 1.0 / rate_per_sec
    for ev in events:
        time.sleep(interval)
        yield ev

if __name__ == "__main__":
    events = load_events()
    rate = 5  # eventos por segundo

    # Elige la distribución:
    gen = poisson_rate(events, rate)
    # gen = uniform_rate(events, rate)

    for e in gen:
        print(json.dumps(e, default=json_util.default))
