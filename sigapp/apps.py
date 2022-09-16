from django.apps import AppConfig


# class SigappConfig(AppConfig):
#     default_auto_field = 'django.db.models.BigAutoField'
#     name = 'sigapp'

 
class SigappConfig(AppConfig):
    name = 'sigapp'
 
    def ready(self):
        import sigapp.Signals