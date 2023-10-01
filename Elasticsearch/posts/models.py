from django.db import models

class ElasticDemo(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField()
    