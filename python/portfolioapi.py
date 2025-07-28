from fastapi import FastAPI
import HTTTPException
import random
import json
import os
from pydanti import BaseModel
import uuid import uuid4
from typing import Optional
from fastapi.encoders import jsonable_encoder



app = FastAPI()

class projects (BaseModel):
    name: str
    languague: str
    projects_id: Optional[str] = uuid4().hex

PROJECTS_FILES = "proects.json"

PROJECTS_DATABASE[]

 """
PROJECTS_DATABASE:[
    "Calculdora python",
    "Listas python",
    "1° API"
]
""" 
# type: ignore


if os.path.exist(PROJECTS_FILES):
    with open (PROJECTS_FILES, "r") as f:
        PROJECTS_DATABASE = json.load(f)

# / - boas vindas
@app.get("/")
async def home():
    return "Bem vindo ao meu porfolio"

# projects - projetos
@app.get("/projects")
async def projects():
    return { "projects" : [PROJECTS_DATABASE]}

# /projects/{index} - listar um projeto
app.get("projects/{index}")
async def projects(index: int):
    if index < 0 or index >=  len(PROJECTS_DATABASE):
        raise HTTTPException(404, " Index out of range")
    else:
        return {"projects": PROJECTS_DATABASE[index]}
    
# random - projeto aleatorio
@app.get("random")
async def random(): 
    return random.choice(PROJECTS_DATABASE)

# add - add project
@app.post("add")
async def add(projeto: projects):
    projeto.projects_id = uuid4().hex
    PROJECTS_DATABASE.append(projects)
    json_projects = jsonable_encoder(projeto)
    with open (PROJECTS_FILES, "w") as f:
        json.dump(PROJECTS_FILES, f)
    return {"message": f'project {project} added'}



