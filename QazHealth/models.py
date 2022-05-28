from django.db import models


# Create your models here.
class Symptom(models.Model):
    name = models.CharField(max_length=30)

    def create(self, name):
        self.name = name
        return self


class Note(models.Model):
    address = models.CharField(max_length=100)
    symptom = Symptom.name
    description = models.TextField(max_length=200)

    def create(self, address, symptom, description):
        self.address = address
        self.symptom = symptom
        self.description = description
