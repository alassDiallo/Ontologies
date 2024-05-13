from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_road():
    return {"Hello world"}


@app.get("/donnees")
def donnees():
    return {
        "nom": "DIALLO",
        "Prenom": "Assane"
    }
