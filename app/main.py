from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello SAKSelector!"}

@app.get("/models")
def get_models():
    return [
        {"name": "Huntsman", "size": "91mm", "tools": ["scissors", "saw", "corkscrew"]},
        {"name": "Climber", "size": "91mm", "tools": ["scissors", "corkscrew"]},
        {"name": "Tinker", "size": "91mm", "tools": ["phillips", "awl"]},
    ]
@app.get("/sak/{model_name}")
def get_single_model(model_name: str):
    models = [
        {"name": "Huntsman", "size": "91mm", "tools": ["scissors", "saw", "corkscrew"]},
        {"name": "Climber", "size": "91mm", "tools": ["scissors", "corkscrew"]},
        {"name": "Tinker", "size": "91mm", "tools": ["phillips", "awl"]},
    ]

    for m in models:
        if m["name"].lower() == model_name.lower():
            return m

    return {"error": "Model not found"}
