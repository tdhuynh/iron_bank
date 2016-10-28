from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

PROCESS_TYPE = {
    ("D","Deposit"),
    ("W","Withdrawal"),
}

class Transaction(models.Model):
    account = models.ForeignKey('auth.User')
    amount = models.FloatField(default=0)
    process_type = models.CharField(max_length=1, choices=PROCESS_TYPE)
    created_by = models.DateTimeField(auto_now_add=True)



@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(account=instance)


class Profile(models.Model):
    account = models.OneToOneField('auth.User')

    @property
    def balance(self):
        deposit = 0
        withdraw = 0
        all_transactions = Transaction.objects.filter(account=self.account)
        for transaction in all_transactions:
            if transaction.process_type == 'W':
                withdraw += transaction.amount
            else:
                deposit += transaction.amount
        return round(deposit - withdraw, 2)
