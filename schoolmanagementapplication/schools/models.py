from django.db import models


class School(models.Model):
    schoolId = models.CharField(max_length=20)
    name = models.CharField(max_length=30)
    email = models.EmailField()
    contact = models.CharField(max_length=15)

    class Meta:
        db_table = "scl"
