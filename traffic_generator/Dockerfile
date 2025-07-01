FROM python:3.10-slim

WORKDIR /app

COPY traffic_generator.py .

RUN pip install pymongo

CMD ["python", "traffic_generator.py"]
