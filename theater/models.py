import uuid
from django.utils import timezone
from django.db import models
from timezone_field import TimeZoneField


class Vars(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    field = models.CharField(max_length=64)
    value = models.CharField(max_length=64)
    ref = models.ForeignKey('self', related_name='group',
                            on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.value

    @staticmethod
    def getOptions(fieldName, ref=None):
        return Vars.objects.filter(field=fieldName, ref__value=ref)

    class Meta:
        verbose_name = 'Variables'
        verbose_name_plural = 'Variables'
        ordering = ['field', 'value']
        indexes = [
            models.Index(fields=['field'])
        ]


class MediaServer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.ForeignKey(Vars, related_name='vendor', on_delete=models.SET_NULL,
                               null=True, blank=True, limit_choices_to={'field': 'mediaserver.vendor'},
                               verbose_name='Mediaserver Vendor')
    model = models.ForeignKey(Vars, related_name='model', on_delete=models.SET_NULL,
                              null=True, blank=True, limit_choices_to={'field': 'mediaserver.model'},
                              verbose_name='Mediaserver Model')
    sw_ver = models.CharField(
        verbose_name='Hardware/Software version', max_length=64, blank=True, null=True)
    serial = models.CharField(
        verbose_name='Serial Number', max_length=64, unique=True)
    certificate = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.vendor or ""} {self.model or ""} {self.serial}'


class Projector(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    vendor = models.CharField(
        verbose_name='Projector Vendor', max_length=64, blank=True, null=True)
    model = models.CharField(
        verbose_name='Projector Model', max_length=64, blank=True, null=True)
    sw_ver = models.CharField(
        verbose_name='Hardware/Software version', max_length=64, blank=True, null=True)
    serial = models.CharField(
        verbose_name='Serial Number', max_length=64, unique=True)
    icp_certificate = models.TextField(blank=True, null=True)
    ld_certificate = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.vendor} {self.model}'


class Theater(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    name_int = models.CharField(max_length=64, blank=True, null=True)
    circuit = models.CharField(max_length=64, blank=True, null=True)
    street = models.CharField(max_length=256, blank=True, null=True)
    city = models.CharField(max_length=64, blank=True, null=True)
    state = models.CharField(max_length=32, blank=True, null=True)
    postal = models.CharField(max_length=16, blank=True, null=True)
    country = models.CharField(max_length=8, blank=True, null=True)

    contact_name = models.CharField(max_length=64, blank=True, null=True)
    contact_phone = models.CharField(max_length=64, blank=True, null=True)
    contact_email = models.EmailField(blank=True, null=True)

    timezone = TimeZoneField(
        choices_display='WITH_GMT_OFFSET', default=timezone.get_current_timezone)
    comments = models.TextField(verbose_name='Comments', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        return f'{self.name} ({self.screens.count()})'

    class Meta:
        ordering = ['name']
        indexes = [
            models.Index(fields=['name'])
        ]


class Screen(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(verbose_name='Screen name/number', max_length=64)
    theater = models.ForeignKey(
        Theater, related_name='screens', on_delete=models.CASCADE, default=None)

    projector_pri = models.OneToOneField(Projector, verbose_name='Primary projector',
                                         related_name='projector_pri', on_delete=models.SET_NULL,
                                         null=True, blank=True)
    projector_sec = models.OneToOneField(Projector, verbose_name='Secondary projector',
                                         related_name='projector_sec', on_delete=models.SET_NULL,
                                         null=True, blank=True)
    mediaserver_pri = models.OneToOneField(MediaServer, verbose_name='Primary mediaserver',
                                           related_name='mediaserver_pri', on_delete=models.SET_NULL,
                                           null=True, blank=True)
    mediaserver_sec = models.OneToOneField(MediaServer, verbose_name='Secondary mediaserver',
                                           related_name='mediaserver_sec', on_delete=models.SET_NULL,
                                           null=True, blank=True)
    is_dual = models.BooleanField(default=False)

    audio_type = models.CharField(max_length=32, blank=True, null=True)
    motin_fx = models.CharField(max_length=32, blank=True, null=True)
    aspect_ratio = models.CharField(max_length=32, blank=True, null=True)
    screen_mask = models.CharField(max_length=32, blank=True, null=True)
    s3d_type = models.CharField(max_length=32, blank=True, null=True)
    s3d_brightness = models.CharField(max_length=32, blank=True, null=True)
    film_35mm = models.BooleanField(default=False)
    integrator = models.CharField(max_length=32, blank=True, null=True)
    inst_date = models.DateField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False)

    def __str__(self):
        if hasattr(self, 'theater'):
            return f'{self.theater.name}-Screen {self.name}'
        else:
            return self.name
