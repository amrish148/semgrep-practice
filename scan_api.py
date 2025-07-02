import json
from fastapi import FastAPI, Form
from fastapi.responses import JSONResponse
import subprocess
import os

app = FastAPI()

@app.post("/scan/")
def scan_local_repo(
    code_path: str = Form(...), 
    config_path: str = Form(...)
):
    if not os.path.isdir(code_path):
        return JSONResponse(status_code=400, content={"error": "Invalid code_path"})

    if not os.path.isfile(config_path):
        return JSONResponse(status_code=400, content={"error": "Invalid config_path"})

    try:
        result = subprocess.run(
            ["semgrep", "--json", "--config", config_path, code_path],
            capture_output=True, text=True, check=True
        )
        return JSONResponse(content=json.loads(result.stdout))
    except subprocess.CalledProcessError as e:
        return JSONResponse(status_code=500, content={"error": e.stderr})
