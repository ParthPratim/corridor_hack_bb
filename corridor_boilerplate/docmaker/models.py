from django.db import models

class ModelDetails(models.Model):
    doc_id = models.BigAutoField(primary_key=True)
    devname = models.CharField(max_length=100)
    modelname = models.CharField(max_length=100)
    overview = models.CharField(max_length=100)
    reason = models.CharField(max_length=100)
    

    class Meta:
        verbose_name = "ModelDetails"