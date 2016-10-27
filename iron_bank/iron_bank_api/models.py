from django.db import models

PROCESS_TYPE = {
    ("D","deposit"),
    ("W","withdrawal"),
}

class Transaction(models.Model):
    account = models.ForeignKey('auth.User')
    amount = models.FloatField()
    process_type = models.CharField(max_length=1, choices=PROCESS_TYPE)


# no balance stored, instead, return total of all transactions
