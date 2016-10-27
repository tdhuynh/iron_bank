from django.conf.urls import url, include
from django.contrib import admin
from iron_bank_api.views import IndexCreateView, TransactionListCreateAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^obtain_token/$', obtain_auth_token),
    url(r'^$', IndexCreateView.as_view(), name="index_create_view"),
    url(r'^transaction/$', TransactionListCreateAPIView.as_view(), name="transaction_list_create_api_view"),
]
