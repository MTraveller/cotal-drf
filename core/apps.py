from django.apps import AppConfig


class CoreConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'core'

    def ready(self):
        import core.signals.handlers
        from core.signals import initial_db

        initial_db.send_robust(sender='initial', name='initial')
