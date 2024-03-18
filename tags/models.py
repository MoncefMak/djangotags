from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=50)
    color_text = models.CharField(max_length=255)
    description = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.tag
