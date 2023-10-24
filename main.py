import os
import io
import uvicorn
import replicate
from config import MODEL
from pathlib import Path
from fastapi.staticfiles import StaticFiles
from fastapi import FastAPI, Request, Form, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# Mount the "static" and "tmp" directories for serving static files
app.mount("/static", StaticFiles(directory=Path(__file__).parent / "static"), name="static")
app.mount("/tmp", StaticFiles(directory="tmp"), name="tmp")

templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def read_data(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.post("/submit")
async def generate_recipe(
        request: Request,
        image: str = Form(...),
        description: str = Form(...),
        image_file: UploadFile = File(...),
):
    img_data = await image_file.read()

    with open(f'tmp/{image_file.filename}', "wb") as file:
        file.write(img_data)
        file.close()

    img_bytes = open(f'tmp/{image_file.filename}', "rb")
    output = replicate.run(
        MODEL,
        input={"image": img_bytes, "prompt": description}
    )
    recipe = ""
    for item in output:
        recipe += item
    # print(recipe)
    return templates.TemplateResponse("recipe.html", {"request": request, "image": img_data, "text": description,
                                                      "filename": image_file.filename, "recipe": recipe})


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
