from fastapi import FastAPI
from fastapi import FastAPI,Request,Depends,Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse,JSONResponse
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Form

app = FastAPI()
templates=Jinja2Templates(directory="templates")
app.mount("/templates", StaticFiles(directory="templates"), name="templates")



from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
async def get_order(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@app.get('/login', response_class=HTMLResponse)
async def get_order(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.get('/dashboard', response_class=HTMLResponse)
async def get_order(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})



@app.get('/order', response_class=HTMLResponse)
async def get_order(request: Request):
    return templates.TemplateResponse("order.html", {"request": request})



@app.get('/explore', response_class=HTMLResponse)
async def get_order(request: Request):
    return templates.TemplateResponse("explore.html", {"request": request})



@app.get('/hotal', response_class=HTMLResponse)
async def get_order(request: Request):
    return templates.TemplateResponse("hotal.html", {"request": request})


@app.get('/cart', response_class=HTMLResponse)
async def get_order(request: Request):
    return templates.TemplateResponse("cart.html", {"request": request})



@app.get('/profile', response_class=HTMLResponse)
async def get_order(request: Request):
    return templates.TemplateResponse("profile.html", {"request": request})


@app.get('/payment', response_class=HTMLResponse)
async def get_order(request: Request):
    return templates.TemplateResponse("payment.html", {"request": request})
