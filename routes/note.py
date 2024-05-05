
from fastapi import Request, APIRouter
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from config.db import connection  # Assuming this is the correct import for your database connection
from models.note import Note  # Assuming this is the correct import for your Note model

note_router = APIRouter()
templates = Jinja2Templates(directory="templates")


@note_router.get('/', response_class=HTMLResponse)
async def index(request: Request):
    docs = connection.notes.notes.find({})
    newDoc = []
    for doc in docs:
        newDoc.append({
            "id": doc["_id"],
            "note": doc["note"],
        })
    return templates.TemplateResponse(
        "index.html", {"request": request, "newDoc": newDoc}
    )


@note_router.post('/', response_class=HTMLResponse)
async def add_note(request: Request):
    form_data = await request.form()
    formDict = dict(form_data)
    note_content = connection.notes.notes.insert_one(formDict)
    return HTMLResponse(content="<h1>Success</h1>", status_code=200)

