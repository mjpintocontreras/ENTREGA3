Entrega 3 - Sistemas Distribuidos
Proyecto de visualización del tráfico en la Región Metropolitana usando Elasticsearch y Kibana

Estructura
scraper/
pig/
traffic_generator/
docker-compose.yml
informe.pdf

Uso
git clone https://github.com/mjpintocontreras/ENTREGA3.git
cd ENTREGA3
docker-compose up --build
python3 pig/cargar_a_elasticsearch.py

Acceder a Kibana en: http://localhost:5601
