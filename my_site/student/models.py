from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    age = models.IntegerField()
    phone = models.CharField(max_length=200)

    def __str__(self):
        return "%s %s %i %i %i"(
            self.first_name,
            self.last_name,
            self.age,
            self.phone,
            self.id,
        )
