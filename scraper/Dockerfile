FROM python:3.10-slim

WORKDIR /app

COPY scraper_waze_api.py .

RUN pip install pymongo requests

CMD ["python", "scraper_waze_api.py"]
