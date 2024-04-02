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
def get_test(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("test.html", {"request": request})



@app.get('/home')
def get_home(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("home.html", {"request": request})



@app.get('/login')
def get_login(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/logcheck")
def logcheck(request:Request,db:Session=Depends(get_db),login_user:str=Form(...),login_password:str=Form(...)):
    print(login_user,login_password)
    find=db.query(models.SignUp).filter(models.SignUp.username==login_user,models.SignUp.password==login_password).first()
    if find is None:
        error= "Invalid Username or Password!"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)
    else:
        error= "Done"   
        json_compatible_item_data = jsonable_encoder(error)
        return JSONResponse(content=json_compatible_item_data)



@app.get('/dashboard')
def get_dashboard(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("dashboard.html", {"request": request})



@app.get('/order')
def get_order(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("order.html", {"request": request})



@app.get('/explore')
def get_explore(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("explore.html", {"request": request})



@app.get('/hotal')
def get_hotal(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("hotal.html", {"request": request})


@app.get('/cart')
def get_cart(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("cart.html", {"request": request})



@app.get('/profile')
def get_profile(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("profile.html", {"request": request})


@app.get('/payment')
def get_payment(request: Request, db: Session = Depends(get_db)):
    return templates.TemplateResponse("payment.html", {"request": request})