from django.shortcuts import render
from iron_bank_api.models import Transaction
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.forms import User
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("index_create_view")


class IndexCreateView(CreateView):
    model = Transaction
    success_url = reverse_lazy("index_create_view")
    fields = ('amount', 'process_type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transaction_list"] = Transaction.objects.all()
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.account = self.request.user

        return super().form_valid(form)


    # def balance(self):
    #     all_transactions = Transaction.objects.filter(account=self.request.user.id)
    #     for transaction in all_transactions:
    #         if transaction.process_type == "W":
    #             withdraw = transaction.amount * -1
    #         else:
    #             deposit = transaction.amount
    #         return sum(deposit) + sum(withdraw)



class TransactionListCreateAPIView(ListCreateAPIView):
    pass
    # def get_queryset(self):
    #     return Transaction.objects.filter(account=self.request.user)
    #
    # def balance(self):
    #     all_transactions = Transaction.objects.filter(account=self.request.user)
