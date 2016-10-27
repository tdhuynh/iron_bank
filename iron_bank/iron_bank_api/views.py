from django.shortcuts import render
from iron_bank_api.models import Transaction
from django.views.generic.edit import CreateView
from rest_framework.generics import ListCreateAPIView
from django.urls import reverse_lazy


class IndexCreateView(CreateView):
    model = Transaction
    success_url = reverse_lazy("index_create_view")
    fields = ('amount', 'process_type')


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transaction_list"] = Transaction.objects.filter(account=self.request.user)
        return context

    def get_queryset(self):
        return Transaction.objects.filter(account=self.request.user)

    def balance(self):
        all_transactions = Transaction.objects.filter(account=self.request.user)
        for transaction in all_transactions:
            if transaction.process_type == "W":
                withdraw = transaction.amount * -1
            else:
                deposit = transaction.amount
            return sum(deposit) + sum(withdraw)




class TransactionListCreateAPIView(ListCreateAPIView):
    pass
    # def get_queryset(self):
    #     return Transaction.objects.filter(account=self.request.user)
    #
    # def balance(self):
    #     all_transactions = Transaction.objects.filter(account=self.request.user)
