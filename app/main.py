from fastapi import FastAPI

app = FastAPI()

# ---------------------------------------------------------
# Shared model data (all endpoints use this)
# ---------------------------------------------------------
models = [
    {"name": "Huntsman", "size": "91mm", "tools": ["scissors", "saw", "corkscrew"]},
    {"name": "Climber", "size": "91mm", "tools": ["scissors", "corkscrew"]},
    {"name": "Tinker", "size": "91mm", "tools": ["phillips", "awl"]},
]

# ---------------------------------------------------------
# Root endpoint
# ---------------------------------------------------------
@app.get("/")
def root():
    return {"message": "Hello SAKSelector!"}

# ---------------------------------------------------------
# Return all models
# ---------------------------------------------------------
@app.get("/models")
def get_models():
    return models

# ---------------------------------------------------------
# Return a single model by name
# ---------------------------------------------------------
@app.get("/sak/{model_name}")
def get_single_model(model_name: str):
    for m in models:
        if m["name"].lower() == model_name.lower():
            return m
    return {"error": "Model not found"}

# ---------------------------------------------------------
# Search models by tool
# ---------------------------------------------------------
@app.get("/search")
def search_models(tool: str):
    results = []
    for m in models:
        if tool.lower() in [t.lower() for t in m["tools"]]:
            results.append(m)
    return results
