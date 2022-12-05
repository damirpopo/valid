from django.apps import AppConfig


class InvalidConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'invalid'
