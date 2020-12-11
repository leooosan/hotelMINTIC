from fastapi import FastAPI
from db.db_reservas import lista_reservas
from fastapi import HTTPException
from db.db_reservas import Reserva

app = FastAPI()


@app.get("/") 
async def root():
    return {"message": "Bienvenidos Hotel Mintic"}

@app.get("/reserva/") 
async def reserva():# funcion root
    return {"message": lista_reservas}

@app.get("/reserva/{reserva}")
async def get_reserva_by_reserva(reserva : str):# funcion reserva
    if username in lista_reservas:
        return {"message": lista_reservas[reserva]}
    raise HTTPException(status_code = 404, detail="la reserva no existe!")

@app.post("/reserva/")
async def crear_reserva(reserva : Reserva):
    lista_reservas[reserva.Reserva]= reserva
    return reserva

@app.delete("/reserva/")
async def crear_reserva(reserva : Reserva):
    del lista_reservas[reserva.Reserva]
    return reserva

@app.put("/reserva/")
async def crear_reserva(user : Reserva):
    lista_reservas[user.Reserva]= reserva
    return reserva