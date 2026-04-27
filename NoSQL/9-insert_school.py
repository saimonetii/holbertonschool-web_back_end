#!/usr/bin/env python3
""" Modulo para insertar un nuevo documento en una coleccion """

def insert_school(mongo_collection, **kwargs):
    """
    Inserta un documento basado en los kwargs pasados a la funcion.
    Retorna el _id del documento recien creado.
    """
    nuevo_documento = mongo_collection.insert_one(kwargs)
    return nuevo_documento.inserted_id
