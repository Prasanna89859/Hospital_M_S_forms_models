from django.db import models

# Create your models here.
class department(models.Model):
    name=models.CharField(max_length=100)
    slocation=models.CharField(max_length=100)
    def __str__(self):
        return self.name
class Doctor(models.Model):
    name=models.CharField(max_length=100)
    department=models.ForeignKey(department,on_delete=models.CASCADE)
    def __str__(self):
        return self.name
class patient(models.Model):
    name=models.CharField(max_length=100)
    tnumber=models.IntegerField()
    dob=models.DateField()
    def __str__(self):
        return self.name
class AM(models.Model):
    Doctor=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient=models.ForeignKey(patient,on_delete=models.CASCADE)
    date_time=models.DateField()  