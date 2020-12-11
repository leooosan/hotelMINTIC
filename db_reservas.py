from pydantic import BaseModel
from datetime import date


class Reserva(BaseModel):
    id: int
    quien_reserva: str
    telefono: str
    fecha_entrada: date
    fecha_salida: date
    numero_noches: int
    tipo_habitacion: str
    numero_personas: int
    numero_habitacion: int
    precio: int


Reserva ={
    1: Reserva(id=1, quien_reserva = "Juan Peréz", fecha_entrada= "13/12/2020", fecha_salida="18/12/2020", numero_noches= 5, tipo_habitacion="Doble", numero_personas=2, numero_habitacion=305, precio=690000),
    2: Reserva(id=2, quien_reserva = "Mario Gomez", fecha_entrada= "20/12/2020", fecha_salida="06/01/2021", numero_noches= 17, tipo_habitacion="Sencilla", numero_personas=1, numero_habitacion=108, precio=1750000),
    3: Reserva(id=3, quien_reserva = "Camila Reyes", fecha_entrada= "03/01/2021", fecha_salida="23/01/2021", numero_noches= 20, tipo_habitacion="Suit", numero_personas=2, numero_habitacion=501, precio=3100000)
}

def todas_reservas ():
    lista_reservas =[]
    for e in Reserva:
        lista_reservas.append(Reserva[e])
        return lista_reservas

def crear_reserva(reserva:Reserva):
    if reserva.id in Reserva:
        return False
    else: 
        Reserva[reserva.id] = reserva
        return True



