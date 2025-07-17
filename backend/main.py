from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from services.script_generator import generate_script

app = FastAPI()

class PromptInput(BaseModel):
    prompt: str

@app.get("/")
def read_root():
    return {"message": "🎉 Faceless AI Video Backend is running!"}

@app.post("/generate-script")
def script_endpoint(data: PromptInput):
    script = generate_script(data.prompt)
    if "Error:" in script:
        raise HTTPException(status_code=500, detail=script)
    return {"script": script}
