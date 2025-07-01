-- Cargar los datos desde el CSV
eventos = LOAD 'datos/eventos.csv' 
    USING PigStorage(',')
    AS (tipo:chararray, subtipo:chararray, comuna:chararray, calle:chararray, timestamp:long);

-- Eliminar eventos con campos vacíos
limpios = FILTER eventos BY tipo IS NOT NULL AND comuna IS NOT NULL AND timestamp IS NOT NULL;

-- Normalizar texto a minúscula (ya lo hicimos en Python, así que este paso es opcional)

-- Agrupar por comuna
por_comuna = GROUP limpios BY comuna;

-- Contar cuántos eventos hay por comuna
cuenta_comuna = FOREACH por_comuna GENERATE group AS comuna, COUNT(limpios) AS cantidad;

-- Guardar resultados
STORE cuenta_comuna INTO 'salidas/eventos_por_comuna' USING PigStorage(',');

-- Contar eventos por tipo
por_tipo = GROUP limpios BY tipo;
cuenta_tipo = FOREACH por_tipo GENERATE group AS tipo, COUNT(limpios) AS cantidad;
STORE cuenta_tipo INTO 'salidas/eventos_por_tipo' USING PigStorage(',');

-- Contar eventos por subtipo
por_subtipo = GROUP limpios BY subtipo;
cuenta_subtipo = FOREACH por_subtipo GENERATE group AS subtipo, COUNT(limpios) AS cantidad;
STORE cuenta_subtipo INTO 'salidas/eventos_por_subtipo' USING PigStorage(',');

