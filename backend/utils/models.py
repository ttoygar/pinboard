from django.db import models

class BaseModel(models.Model):
    """
    An abstract base class model that provides self-
    updating 'created_date' and 'modified_date' fields.
    """
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True