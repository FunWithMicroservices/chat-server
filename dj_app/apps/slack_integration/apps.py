from django.apps import AppConfig


class SlackIntegrationConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.slack_integration'

    def ready(self):
        import apps.slack_integration.signals as signals
        __all__ = ('signals', )
