from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=1, max_length=50)
    email: EmailStr
    password: str = Field(min_length=8)

class TareaSchema(BaseModel):
    titulo: str = Field(min_length=1, max_length=100)
    descripcion: Optional[str] = Field(max_length=200)
    prioridad: str = "media"
    clasificacion: str = "personal"