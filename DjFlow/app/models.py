"""
Definition of models.
"""

from django.db import models

# Create your models here.

class ExpMetadata(models.Model):
    """Experiment metadata"""
    project = models.CharField(max_length=200)
    pi = models.CharField(max_length=200)
    experiment = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model."""
        return self.text
