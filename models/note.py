from pydantic import BaseModel


class Note(BaseModel):
    id: object
    note: str
