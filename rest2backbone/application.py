from rest_framework import serializers, viewsets, routers, fields, six
from rest2backbone.resources import IndexedRouter


APPLICATION = []


def register(namespace, view):
    APPLICATION.append((namespace, view))

def get_router():
    # router = IndexedRouter(trailing_slash=False)
    router = routers.DefaultRouter()

    for namespace, view in APPLICATION:
        print namespace, view
        router.register(namespace, view, base_name=namespace)
        view.namespace = namespace

    return router

def get_model_views():
    return APPLICATION
