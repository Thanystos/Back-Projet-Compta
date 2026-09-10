from pydantic import BaseModel

class DepenseBase(BaseModel):
    nom: str

class DepenseCreate(DepenseBase):
    pass

class DepenseRead(DepenseBase):
    id: int

    class Config:
        orm_mode = True
