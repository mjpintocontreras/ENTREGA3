import csv
from elasticsearch import Elasticsearch, helpers

# Conectar a Elasticsearch en localhost
es = Elasticsearch("http://localhost:9200")

def cargar_csv_a_elasticsearch(nombre_archivo, indice):
    with open(nombre_archivo, encoding='utf-8') as f:
        reader = csv.reader(f)
        acciones = [
            {
                "_index": indice,
                "_source": {
                    "comuna": row[0],
                    "cantidad": int(row[1])
                }
            }
            for row in reader
        ]
        helpers.bulk(es, acciones)
        print(f"✅ Se cargaron {len(acciones)} registros al índice '{indice}'")

# Cargar cada CSV en su índice correspondiente
cargar_csv_a_elasticsearch("eventos_comuna.csv", "eventos_comuna")


def cargar_csv_a_elasticsearch_eventos_tipo(nombre_archivo, indice):
    with open(nombre_archivo, encoding='utf-8') as f:
        reader = csv.DictReader(f, fieldnames=["tipo", "cantidad"])
                # Crear índice con mapping correcto (tipo: keyword, cantidad: integer)
        es.indices.create(
            index=indice,
            ignore=400,
            body={
                "mappings": {
                    "properties": {
                        "tipo": {"type": "keyword"},
                        "cantidad": {"type": "integer"}
                    }
                }
            }
        )
        acciones = [
            {
                "_index": indice,
                "_source": {
                   "tipo": row["tipo"],
                   "cantidad": int(row["cantidad"])
                }
            }
            for row in reader
        ]
        helpers.bulk(es, acciones)
        print(f"✅ Se cargaron {len(acciones)} registros al índice '{indice}'")

cargar_csv_a_elasticsearch_eventos_tipo("eventos_tipo.csv", "eventos_tipo")



def cargar_csv_a_elasticsearch_eventos_subtipo(nombre_archivo, indice):
    with open(nombre_archivo, encoding='utf-8') as f:
        reader = csv.DictReader(f, fieldnames=["subtipo", "cantidad"])

        # Crear índice con mapping correcto
        es.indices.create(
            index=indice,
            ignore=400,
            body={
                "mappings": {
                    "properties": {
                        "subtipo": {"type": "keyword"},
                        "cantidad": {"type": "integer"}
                    }
                }
            }
        )

        acciones = [
            {
                "_index": indice,
                "_source": {
                    "subtipo": row["subtipo"],
                    "cantidad": int(row["cantidad"])
                }
            }
            for row in reader
        ]
        helpers.bulk(es, acciones)
        print(f"✅ Se cargaron {len(acciones)} registros al índice '{indice}'")

cargar_csv_a_elasticsearch_eventos_subtipo("eventos_subtipo_traducido.csv", "eventos_subtipo")
