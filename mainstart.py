from fastapi import FastAPI
from pynput.keyboard import Controller, Key

from main import appends
from fastapi import FastAPI, Form, Request
from fastapi.templating import Jinja2Templates
from package import pack
import models
from database import engine
from fastapi import FastAPI, Form, Request, Depends
import time

app = FastAPI(openapi_url="/api/openapi.json", docs_url="/api/docs")

templates = Jinja2Templates(directory="templates")
templates.env.globals.update(enumerate=enumerate)

app.include_router(appends, prefix="/api")
app.include_router(pack, prefix="/package")
models.Base.metadata.create_all(bind=engine)

@app.get("/pack/")
def 누른_작동버튼():
    from pynput.keyboard import Key, Controller
    time.sleep(3)
    keyboard = Controller()
    keyboard.press('a')

    # Press and release space
    keyboard.press(Key.tab)
    keyboard.release(Key.tab)
    keyboard.press('a')


@app.get("/")
async def render_upload_form(request: Request):
    return templates.TemplateResponse("main.html", {"request": request})
