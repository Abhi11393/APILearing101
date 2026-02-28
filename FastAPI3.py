from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import FastAPI,Request

app = FastAPI()
templetes = Jinja2Templates(directory="templates")

@app.get("/hello/",response_class=HTMLResponse)
async def hello(request: Request):
    return templetes.TemplateResponse("hello.html",{"request":request})