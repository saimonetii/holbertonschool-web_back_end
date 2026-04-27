#!/usr/bin/env python3
""" Modulo para listar todos los documentos en una coleccion de MongoDB """

def list_all(mongo_collection):
    """
    Retorna una lista vacia si no hay documentos, 
    de lo contrario retorna todos los documentos en la coleccion
    """
    return [doc for doc in mongo_collection.find()]
