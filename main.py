from fastapi import FastAPI
from fastapi import FastAPI,Request,Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,JSONResponse
from database import SessionLocal
from fastapi.encoders import jsonable_encoder
from sqlalchemy.orm import Session
import models
from fastapi import Form

app = FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")



def get_db():
    db=None
    try:
        db=SessionLocal()
        yield db
    finally:
        db.close()


@app.get('/test')
def get_home(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("test.html", {"request": request})