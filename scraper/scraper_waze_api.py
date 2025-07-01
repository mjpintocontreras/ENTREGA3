# scraper_waze_api.py

import time
import requests
from pymongo import MongoClient
from requests.exceptions import JSONDecodeError

# subdivisión 4×4 de la RM (lat −33.20→−33.80, lon −70.95→−70.30)
lat_steps = [-33.20, -33.35, -33.50, -33.65, -33.80]
lon_steps = [-70.95, -70.80, -70.65, -70.50, -70.30]
bboxes = [(lat_steps[i], lat_steps[i+1], lon_steps[j], lon_steps[j+1])
          for i in range(4) for j in range(4)]

# Mongo
cliente   = MongoClient('mongodb', 27017)
db        = cliente['waze']
coleccion = db['eventos']

def fetch_georss(top, bottom, left, right):
    url = (
      "https://www.waze.com/live-map/api/georss"
      f"?top={top}&bottom={bottom}&left={left}&right={right}"
      "&env=row&types=alerts,traffic"
    )
    try:
        r = requests.get(url, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data.get("alerts", []) + data.get("traffic", [])
    except (JSONDecodeError, requests.RequestException):
        return []

def fetch_rt(top, bottom, left, right):
    url = "https://www.waze.com/web-events"
    body = {
      "boundingBox": [left, bottom, right, top],
      "clientVersion": "25.14.3",
      "types": ["JAM", "ALERT", "CLOSURE", "IRREGULARITY"]
    }
    try:
        r = requests.post(url, json=body, timeout=10)
        r.raise_for_status()
        data = r.json()
        return data.get("features", [])
    except (JSONDecodeError, requests.RequestException):
        return []

while True:
    total_nuevos = 0

    for idx, (top, bottom, left, right) in enumerate(bboxes, start=1):
        geo_items = fetch_georss(top, bottom, left, right)
        rt_items  = fetch_rt(top, bottom, left, right)
        items     = geo_items + rt_items

        print(f"🔄 BBOX {idx}/{len(bboxes)} ({top},{bottom},{left},{right}): {len(items)} items")

        nuevos = 0
        for it in items:
            if "id" in it and not coleccion.find_one({"id": it["id"]}):
                coleccion.insert_one(it)
                nuevos += 1

        total_nuevos += nuevos
        if nuevos:
            print(f"✅  BBOX {idx}: Guardados {nuevos} nuevos")

    if total_nuevos == 0:
        print("⚪  Ningún evento nuevo en este ciclo")

    time.sleep(10)
