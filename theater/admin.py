from django.contrib import admin

from .models import Theater, Screen, Vars, MediaServer, Projector

admin.site.register(Theater)
admin.site.register(Screen)
admin.site.register(Vars)
admin.site.register(MediaServer)
admin.site.register(Projector)
