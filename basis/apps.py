from django.apps import AppConfig


class BasisConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'basis'

    def ready(self):
        from . import signals
