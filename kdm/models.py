from django.utils import timezone
from django.db import models
import uuid
from datetime import timedelta

from movie.models import CPL, Movie
from theater.models import MediaServer, Screen

def _now_plus_one_day():
    return timezone.now() + timedelta(days=1)

class KDM(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name ='KDM name', max_length=256, unique=True)
    cpl = models.ForeignKey(CPL, verbose_name='CPL', on_delete=models.SET_NULL, null=True)

    screen = models.ForeignKey(Screen, on_delete=models.SET_NULL, null=True)
    mediaserver = models.ForeignKey(MediaServer, on_delete=models.SET_NULL, null=True)
    
    TDL_content = models.TextField(null=True)
    KDM_content = models.TextField(null=True)
    date_start = models.DateTimeField(verbose_name='Start Key Validity', default=timezone.now)
    date_end = models.DateTimeField(verbose_name='End Key Validity', default=_now_plus_one_day)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return "{} {}".format(self.cpl.movie.title, self.name)

    class Meta:
        default_permissions = ('add', 'view')
        verbose_name = "KDM"
