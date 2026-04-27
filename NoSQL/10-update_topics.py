#!/usr/bin/env python3
""" Modulo para actualizar los temas (topics) de un documento """

def update_topics(mongo_collection, name, topics):
    """
    Cambia todos los topics de un documento de escuela basado en el nombre
    """
    mongo_collection.update_many(
        { "name": name },
        { "$set": { "topics": topics } }
    )
