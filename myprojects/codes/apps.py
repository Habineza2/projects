from django.apps import AppConfig


class Code1Config(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'codes'
    def ready(self):
        import codes.signals