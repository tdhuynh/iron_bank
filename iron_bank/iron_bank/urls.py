from django.conf.urls import url, include
from django.contrib import admin
from iron_bank_api.views import IndexView, UserCreateView, TransactionCreateView, TransactionListCreateAPIView, TransactionDetailAPIView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^obtain_token/$', obtain_auth_token),
    url(r'^create_user/$', UserCreateView.as_view(), name='user_create_view'),
    url(r'^$', IndexView, name="index_view"),
    url(r'^transactions/$', TransactionCreateView.as_view(), name="transaction_create_view"),
    url(r'^api/transactions/$', TransactionListCreateAPIView.as_view(), name="transaction_list_create_api_view"),
    url(r'^api/transactions/(?P<pk>\d+)/$', TransactionDetailAPIView.as_view(), name="transaction_detail_api_view"),
]
