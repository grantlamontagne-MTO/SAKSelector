from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

# ---------------------------------------------------------
# Template loader (for /ui)
# ---------------------------------------------------------
templates = Jinja2Templates(directory="templates")

# ---------------------------------------------------------
# Shared model data
# ---------------------------------------------------------
models = [
    {"name": "Huntsman", "size": "91mm", "tools": ["scissors", "saw", "corkscrew"]},
    {"name": "Climber", "size": "91mm", "tools": ["scissors", "corkscrew"]},
    {"name": "Tinker", "size": "91mm", "tools": ["phillips", "awl"]},
]

# ---------------------------------------------------------
# UI route
# ---------------------------------------------------------
@app.get("/ui", response_class=HTMLResponse)
def ui_page(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

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
