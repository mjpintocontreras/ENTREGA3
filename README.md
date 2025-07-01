Entrega 3 - Sistemas Distribuidos
Proyecto de visualización del tráfico en la Región Metropolitana usando Elasticsearch y Kibana

Estructura
scraper/
pig/
traffic_generator/
visualizaciones_kibana/
docker-compose.yml

Uso
git clone https://github.com/mjpintocontreras/ENTREGA3.git
cd ENTREGA3
docker-compose up --build
python3 pig/cargar_a_elasticsearch.py



Accede a Kibana en: http://localhost:5601
ve a stack management luego a kibana en saved objects seleccionar import:

seleccionar el archivo visualizaciones_kibana/dashboard_tarea3.ndjson
y accede a las visualizaciones directamente en la Dashboards de Kibana.


