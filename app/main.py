from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates

# from src.model import spell_number

app = FastAPI()
templates = Jinja2Templates(directory="/opt/app/templates/")


@app.get('/')
def read_form():
    return 'use /form route'


@app.get("/form")
def form_post(request: Request):
    return templates.TemplateResponse('form.html',
                                      context={'request': request})


@app.post("/calculategrid")
def form_post(request: Request, startrange: int = Form(...), endrange: int = Form(...),
              quantitylevels: int = Form(...), pare: str = Form(...)):
    return pare
    # startrange + endrange + quantitylevels


@app.post("/rungrid")
def form_post(request: Request, deposit: int = Form(...), shoulder: int = Form(...),
              fixation: int = Form(...), ch_long: bool = Form(False), ch_short: bool = Form(False),
              indicator: str = Form(...)):
    return ch_long
    # startrange + endrange + quantitylevels
