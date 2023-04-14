from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.db import engine, meta_data

users = Table ("users", meta_data,
               Column ("id", Integer, primary_key=True), 
               Column ("Cedula", Integer, primary_key=True),
               Column ("Nombre", String(30), nullable=False),
               Column ("Apellido", String(45), primary_key=True),
               Column ("correo", String(60), nullable=False),
               Column ("clave", String(60), nullable=False),
               Column ("Rol", String(60), nullable=False),
               )
meta_data.create_all(engine)
