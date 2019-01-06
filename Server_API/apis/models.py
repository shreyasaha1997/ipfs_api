from django.db import models

class ipfs_details(models.Model):
    Hash = models.CharField(max_length=250, primary_key=True)
    Host_Count = models.IntegerField(default=0)    