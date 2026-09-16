import funciones as fn
from practica import Desarrollador
import json

equipo = [
    Desarrollador("Victor", "Python", 2),
    Desarrollador("Laura", "Angular", 6),
    Desarrollador("Carlos", "FastAPI", 5),
    Desarrollador("Sofia", "Docker", 1)
]



def leer_seniors():
        with open("seniors.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                print(linea.strip())

def escribir_seniors(equipo):
    with open("seniors.txt", "w", encoding="utf-8") as archivo:
        for nombres in equipo:
            archivo.write(f"{nombres}\n")
    #print("Archivo seniors.txt generado con exito")

def guardar_json(datos,ruta):
        with open(ruta,"w",encoding="utf-8") as archivo:
            json.dump(datos,archivo,indent=4) #EL INDENT ES PARA QUE SE VEA BONITO EN EL ARCHIVO JSON

def cargar_json(ruta):
    try:
        with open(ruta,"r",encoding="utf-8") as archivo:
            return json.load(archivo)
    except FileNotFoundError:
        print("El archivo no existe en la ruta especificada.")
        return None
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return None    




def main():
   resultado = fn.filtrar_seniors(equipo)
   payload = {
        "total_equipo": len(equipo),
        "cantidad_seniors": len(resultado),
        "nombres_seniors": resultado
    }
   # escribir_seniors(resultado)
   # leer_seniors()
   guardar_json(payload,"data.json")
   info = cargar_json("data.json")
   print(f"El archivo reporta un total de {info['total_equipo']} desarrolladores y {info['cantidad_seniors']} seniors. los seniors son {', '.join(info['nombres_seniors'])}.")
   print(equipo[0])
if __name__ == "__main__":
    main()