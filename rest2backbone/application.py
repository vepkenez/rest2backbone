from rest_framework import serializers, viewsets, routers, fields, six
from rest2backbone.resources import IndexedRouter


APPLICATION = []


def register(namespace, view):
    APPLICATION.append((namespace, view))

def get_router():
    router = IndexedRouter(trailing_slash=False)

    for namespace, view in APPLICATION:
        router.register(namespace, view, base_name=namespace)
        view.namespace = namespace

    return router

def get_model_views():
    return APPLICATION
