from django.apps import AppConfig


class AzureConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.azure'

    def ready(self):
        import apps.azure.signals as signals
        __all__ = ('signals', )
