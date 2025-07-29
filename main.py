from fastapi import FastAPI, HTTPException
from agent import run_agent_task

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "Agent Task Runner is live!"}

@app.post("/run")
def run_task(prompt: str):
    try:
        result = run_agent_task(prompt)
        return {"response": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
