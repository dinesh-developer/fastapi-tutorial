from fastapi import FastAPI
import json

app = FastAPI()

def load_patients():
    try:
        with open("patients.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


@app.get("/")
def hello():
    return {"message": "Patient Management System API"}


@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application."}


@app.get("/patients")
def get_patients():
    patients = load_patients()
    return {"patients": patients}