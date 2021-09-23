from django.db import models

class Movie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(verbose_name ='Title', max_length=64, unique=True, db_index=True)
    full_title = models.CharField(verbose_name='Full title', max_length=255, blank=True, null=True)
    year = models.IntegerField(verbose_name='Year of release', blank=True, null=True)
    studio = models.CharField(verbose_name ='Production studio', max_length=64, blank=True, null=True)
    director = models.CharField(verbose_name ='Director', max_length=64, blank=True, null=True)
    comments = models.TextField(verbose_name='Comments', blank=True, null=True)
    enabled = models.BooleanField(verbose_name='Enabled', default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class CPL(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(verbose_name ='CPL Name', max_length=256, unique=True, db_index=True)
    movie = models.ForeignKey(Movie, on_delete=models.SET_NULL, null=True)
    language = models.CharField(verbose_name='Language', max_length=2)
    subtitles = models.CharField(max_length=2, blank=True, null=True)
    runtime = models.IntegerField()
    comments = models.TextField(verbose_name='Comments', blank=True, null=True)
    CPL = models.TextField()
    KDM = models.TextField(blank=True, null=True)
    encoded = models.BooleanField(default=False)
    _key = models.BigIntegerField(blank=True, null=True)
    _zip = models.BinaryField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
