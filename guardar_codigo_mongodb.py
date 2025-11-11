from pymongo import MongoClient
from datetime import datetime

# Conexión con MongoDB local
client = MongoClient("mongodb://localhost:27017/")

# Base de datos y colección donde guardarás tus códigos
db = client["repositorio_codigo"]
coleccion = db["codigos"]

# Ejemplo de código (puedes cambiar el contenido por tu propio código real)
codigo_fuente = """from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["tienda_tecnologica"]
productos = db["productos_catalogo"]

print("Conexión exitosa a MongoDB.")
"""

# Documento que se guardará en MongoDB
documento_codigo = {
    "nombre": "conexion_mongodb",
    "lenguaje": "Python",
    "descripcion": "Ejemplo de conexión y acceso a la colección productos_catalogo",
    "codigo": codigo_fuente,
    "fecha_subida": datetime.utcnow()
}

# Insertar el documento en la colección
resultado = coleccion.insert_one(documento_codigo)

print(" Código guardado correctamente en MongoDB con ID:", resultado.inserted_id)
