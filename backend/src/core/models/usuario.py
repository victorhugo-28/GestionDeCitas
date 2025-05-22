from sqlalchemy import Column, Integer, String
from infrastructure.data.AppDbContext import Base

class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    correo = Column(String)
