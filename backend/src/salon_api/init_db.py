from infrastructure.data.AppDbContext import engine, Base
from core.models.cliente import Cliente, Base
from core.models.proveedor import Proveedor, Base
from core.models.tipo_articulo import TipoArticulo, Base
from core.models.articulo import Articulo, Base
from core.models.rol import Rol, Base
from core.models.venta import Venta, Base
from core.models.compra import Compra, Base
# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)
print("Base de datos creada")
