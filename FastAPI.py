from fastapi import FastAPI,Body
from typing import List
from pydantic import BaseModel, Field

app =FastAPI()

class student(BaseModel):
    id:int
    name:str = Field(None,title="Name of Students",max_length=10)
    subject:  List[str] = []


@app.post("/students/")
async def student_data(s1:student):
    return s1
@app.post("/students1/")
async def student_data1(name : str=Body(...), Marks:int=Body(...)):
    return {"name":name,"Marks":Marks}
