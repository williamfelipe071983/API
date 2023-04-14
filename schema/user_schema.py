from pydantic import BaseModel
from typing import Optional 

class UserSchema (BaseModel):
    id: Optional[str]
    cedula: int
    nombre: str
    apellido: str
    correo: str
    clave: str
    Rol: str
    