import urllib.request
import json
import os
from datetime import datetime

# API pública y gratuita para obtener tipos de cambio
URL = "https://open.er-api.com/v6/latest/USD"
JSON_FILE = "historial_tipo_cambio.json"

def get_exchange_rate():
    try:
        # Hacemos la petición a la API
        req = urllib.request.urlopen(URL)
        data = json.loads(req.read())
        
        # Extraemos el tipo de cambio del Colón Costarricense (CRC)
        # La API base es USD, así que esto nos da cuantos colones equivalen a 1 dólar
        return data["rates"].get("CRC")
    except Exception as e:
        print(f"Error al obtener el tipo de cambio: {e}")
        return None

def update_history(rate):
    if not rate:
        return
    
    history = []
    
    # Leer el historial existente si el archivo ya existe
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r", encoding="utf-8") as f:
            try:
                history = json.load(f)
            except json.JSONDecodeError:
                # Si el archivo está vacío o corrupto, empezamos con una lista nueva
                history = []
                
    # Creamos el nuevo registro
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    new_record = {
        "fecha": now,
        "moneda": "USD a CRC",
        "tipo_cambio": rate
    }
    
    # Lo agregamos a la lista
    history.append(new_record)
    
    # Guardamos el historial actualizado en el archivo JSON
    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, indent=4, ensure_ascii=False)
        
    print(f"Historial actualizado exitosamente: {new_record}")

if __name__ == "__main__":
    print("Obteniendo tipo de cambio...")
    rate = get_exchange_rate()
    if rate:
        print(f"Tipo de cambio actual (USD -> CRC): {rate}")
        update_history(rate)
    else:
        print("No se pudo actualizar el historial.")
