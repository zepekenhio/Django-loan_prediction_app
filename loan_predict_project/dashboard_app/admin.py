from django.contrib import admin
from .models import Data

class DataAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'gender', 'mstatus',  'dependance',  'education', 'self_employed', 'appIncome', 'co_appIncome', 'loan_amount', 'loan_amount_term', 'credit_history', 'property_area')

admin.site.register(Data, DataAdmin)
