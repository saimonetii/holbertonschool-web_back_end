#!/usr/bin/env python3
""" Modulo para buscar escuelas por un tema especifico """

def schools_by_topic(mongo_collection, topic):
    """
    Retorna la lista de escuelas que tienen un tema (topic) especifico
    """
    return [doc for doc in mongo_collection.find({ "topics": topic })]
