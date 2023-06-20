from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    date = models.DateField()
    time = models.TimeField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f"Appointment on {self.date} at {self.time} with {self.staff}"
