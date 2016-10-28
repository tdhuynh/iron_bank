from django.shortcuts import render
from iron_bank_api.models import Transaction, Profile
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.views.generic import ListView
from rest_framework.generics import ListCreateAPIView
from django.contrib.auth.forms import User
from django.urls import reverse_lazy


class UserCreateView(CreateView):
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy("index_view")


def IndexView(request):
    context = {
        "all_transactions": Transaction.objects.all(),
    }
    return render(request, 'index.html', context)


class TransactionCreateView(CreateView):
    model = Transaction
    success_url = reverse_lazy("transaction_create_view")
    fields = ('amount', 'process_type')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["transaction_list"] = Transaction.objects.filter(account=self.request.user)
        context["profile_list"] = Profile.objects.filter(account=self.request.user)
        return context

    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.account = self.request.user

        return super().form_valid(form)


class TransactionListCreateAPIView(ListCreateAPIView):
    pass
    # def get_queryset(self):
    #     return Transaction.objects.filter(account=self.request.user)
