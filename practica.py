from dataclasses import dataclass

@dataclass
class Desarrollador:
    nombre: str
    tecnologia: str
    experiencia_anios: int

    def es_senior(self) -> bool:
        return self.experiencia_anios >= 5

#FORMA CLASICA DE HACE UNA CLASE CON EL INIT Y LOS SELF EQUIVALANTE AL THIS
class Desarrollador:
    def __init__(self, nombre, tecnologia, experiencia_anios):
        self.nombre = nombre
        self.tecnologia = tecnologia
        self.experiencia_anios = experiencia_anios
    
    def es_senior(self):
        if self.experiencia_anios >= 5:
            return True
        else:
            return False
        #return self.experiencia_anios >= 5
    
    def obtener_perfil(self):
        return f"Desarrollador {self.nombre}, {self.tecnologia}, {self.es_senior()}"
    
    def __str__(self):
        return f"Dev: {self.nombre} ({self.tecnologia}) - {self.experiencia_anios} años exp"

# Todo lo que esté aquí adentro SOLO correrá si ejecutas practica.py directamente
# pero se ignorará por completo cuando main.py lo importe:
if __name__ == "__main__":  

    nombre = 'Victor'
    añor = 1991
    año_actual = 2026
    edad_calculada = año_actual - añor
    tieneLincia = False
    # Opción 1: En una sola línea con espacios claros
    print(f"Hola, mi nombre es {nombre} y tengo {edad_calculada} años.")

    # Opción 2: Si quieres mostrar los tres datos ordenados en líneas separadas (\n):
    print(f"Nombre: {nombre}\nAño de nacimiento: {añor}\nEdad: {edad_calculada}")

    # Estructura de decisión mutuamente excluyente
    if edad_calculada >= 18 and tieneLincia:
        print("Puede conducir legalmente.")
    elif edad_calculada >= 18 and not tieneLincia:
        print("Tiene la edad requerida pero necesita sacar la licencia.")
    else:
        print("No tiene la edad legal para conducir.")

    lenguajes = ["Python", "JavaScript", "TypeScript"]

    # Acceso por índice (inicia en 0)
    print(lenguajes[-1])  # "Python"

    # Métodos esenciales
    lenguajes.append("SQL")       # Agrega un elemento al final
    lenguajes.remove("JavaScript") # Remueve la primera coincidencia
    cantidad = len(lenguajes)     # Devuelve el tamaño de la lista

    tecnologias = ["JS", "C#","JAVA"]
    tecnologias.append("PHP")
    print(tecnologias[0])
    print(tecnologias[-1])
    print(len(tecnologias))

    numeros = [12, 5, 8, 21, 44, 7, 10]

    for i in numeros:
        if i % 2 == 0:
            print(f"{i} es par")
        else:
            print(f"{i} es impar")

    usuario = {
        "nombre": "Victor",
        "edad": 35,
        "rol": "Developer"
    }

    # Acceso al valor por su clave
    print(usuario["nombre"])  # "Victor"

    # Agregar o modificar claves
    usuario["activo"] = True

    # Acceso seguro con .get() (no rompe el progra

    def calcular_area(base, altura):
        area = (base * altura) / 2
        return area

    resultado = calcular_area(10, 5)
    print(f"Área: {resultado}")

    def presentar_usuario (datos):
        nombre = datos["nombre"]
        tecnologia = datos["Tecnologia"]
        experiencia_anios = datos["experiencia_anios"]
        return f"El desarrollador {nombre} trabaja con: {tecnologia} y tiene años de experiencia {experiencia_anios}"

    empleados = [
        {
        "nombre": "Victor",
        "Tecnologia": "Python",
        "experiencia_anios": "Developer"
        } ,
            {
        "nombre": "Ana",
        "Tecnologia": "C#",
        "experiencia_anios": "Developer"
        } ,   
            {
        "nombre": "Fernando",
        "Tecnologia": "Java",
        "experiencia_anios": "Developer"
        } 
        
    ]

    for emp in empleados:
        if emp["Tecnologia"] == "Python": #se puede usar el GET es recomendado por si una llave no existe no se roma el codigo emp.get("salario", "No especificado")
            print(f"El desarrollador {emp['nombre']} trabaja con {emp['Tecnologia']}")
        else:
            print("Trabaja con otra tecnologia")
        

    usuario_api = {
        "nombre": "Victor",
        # Falta la clave "edad"
        "pais": "Costa Rica"
    }

    try:
        edad = usuario_api["edad"]
        anio_nacimiento = 2026 - edad
        print(f"Año de nacimiento estimado: {anio_nacimiento}")
    except KeyError:
        print("Error: La clave 'edad' no existe.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")




    dev = Desarrollador("Victor", "Python", 2)
    print(dev.obtener_perfil())   

    equipo = [
        Desarrollador("Victor", "Python", 2),
        Desarrollador("Laura", "Angular", 6),
        Desarrollador("Carlos", "FastAPI", 5),
        Desarrollador("Sofia", "Docker", 1)
    ]

    #Qué quiero en la lista final for elemento in origen (if filtro)
    solo_seniors = [dev.nombre for dev in equipo if dev.es_senior()]
    print(solo_seniors)
    print(", ".join(solo_seniors))
    print(*solo_seniors, sep=" - ") #El operador * saca todos los elementos de la lista
    # Imprime directo: Laura - Carlos