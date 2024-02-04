from django.contrib import admin
from .models import *

# Register your models here.

class AdminCustomer(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'address', 'sex', 'age', 'city', 'zip_code')
    
class AdminInvoice(admin.ModelAdmin):
    invoice_date_time = models.DateTimeField(auto_now_add=True)
    list_display = ('customer', 'save_by', 'invoice_date_time', 'last_updated_date', 'paid', 'invoice_type')
    
admin.site.register(Customer, AdminCustomer)
admin.site.register(Invoice, AdminInvoice)
admin.site.register(Article)