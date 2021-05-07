from django.db import models

class Deposit(models.Model):
    deposit = models.CharField(max_length=10)
    term = models.CharField(max_length=10)
    rate = models.CharField(max_length=10)
    interest = models.CharField(max_length=20)