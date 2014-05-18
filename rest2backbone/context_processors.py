from django.conf import settings

from rest2backbone.forms import FormFactory
from . import application


router = application.get_router()
model_views = application.get_model_views()

def context(request):
    return {
        'forms': FormFactory(router),
        'backbone_start_app': getattr(settings, 'BACKBONE_START_APP', None),
        'backbone_models': model_views
    }
