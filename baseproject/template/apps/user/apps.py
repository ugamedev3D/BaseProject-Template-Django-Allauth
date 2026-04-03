from django.apps import AppConfig

class UserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apps.user'

    def ready(self):
        import baseproject.template.apps.user.allauth_override
        import baseproject.template.apps.user.auth.flow_fix
        import baseproject.template.apps.user.signals
