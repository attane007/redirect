from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()

@app.get("/")
async def redirect_to_new_path():
    return RedirectResponse(url="https://www.facebook.com/phonngampittayanukul")
