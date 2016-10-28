from django.contrib import admin
from iron_bank_api.models import Transaction, Profile

admin.site.register([Transaction, Profile])
