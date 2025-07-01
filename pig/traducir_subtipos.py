import csv

# Diccionario de traducción
traducciones = {
    "police_hiding": "policía_oculta",
    "accident_major": "accidente_grave",
    "accident_minor": "accidente_leve",
    "hazard_on_road": "peligro_en_la_vía",
    "hazard_weather": "clima_peligroso",
    "police_visible": "policía_visible",
    "jam_heavy_traffic": "atasco_tráfico_denso",
    "road_closed_event": "evento_calle_cerrada",
    "hazard_on_road_ice": "hielo_en_la_vía",
    "hazard_weather_fog": "niebla_peligrosa",
    "hazard_weather_flood": "inundación",
    "jam_moderate_traffic": "tráfico_moderado",
    "hazard_on_road_object": "objeto_en_la_vía",
    "hazard_on_road_pot_hole": "hoyo_en_la_vía",
    "jam_stand_still_traffic": "tráfico_detenido",
    "hazard_weather_heavy_snow": "nieve_intensa",
    "police_with_mobile_camera": "policía_con_cámara",
    "hazard_on_road_car_stopped": "auto_detenido_en_vía",
    "hazard_on_road_lane_closed": "carril_cerrado",
    "hazard_on_road_construction": "construcción_en_vía",
    "hazard_on_shoulder_car_stopped": "auto_detenido_en_berma",
    "hazard_on_shoulder_missing_sign": "señal_faltante_en_berma",
    "hazard_on_road_traffic_light_fault": "semáforo_mal_funcionamiento",
    "": "(vacío)"
}

# Leer CSV original y escribir el traducido
with open("eventos_subtipo.csv", encoding='utf-8') as entrada, open("eventos_subtipo_traducido.csv", "w", encoding='utf-8', newline='') as salida:
    reader = csv.reader(entrada)
    writer = csv.writer(salida)
    
    for fila in reader:
        subtipo = fila[0]
        cantidad = fila[1]
        traducido = traducciones.get(subtipo, subtipo)  # Usa traducción o el original si no está
        writer.writerow([traducido, cantidad])

print("✅ Archivo 'eventos_subtipo_traducido.csv' generado con traducciones.")
