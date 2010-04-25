from django.db import models

class Discussion(models.Model):
    """A Facebook realtime discussion"""
    owner = models.CharField(max_length=255, db_index=True)
    access_token = models.CharField(max_length=255)
    session_key = models.CharField(max_length=255)
    guid = models.CharField(unique=True, max_length=255, db_index=True)
    topic = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True, verify_exists=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return u"Discussion"
