from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from rest_framework.authtoken.models import Token


PROCESS_TYPE = {
    ("D","Deposit"),
    ("W","Withdrawal"),
}

class Transaction(models.Model):
    account = models.ForeignKey('auth.User')
    amount = models.FloatField(default=0)
    process_type = models.CharField(max_length=1, choices=PROCESS_TYPE)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']


@receiver(post_save, sender='auth.User')
def create_user_profile(**kwargs):
    created = kwargs.get('created')
    instance = kwargs.get('instance')
    if created:
        Profile.objects.create(account=instance)

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
   if created:
       Token.objects.create(user=instance)


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
