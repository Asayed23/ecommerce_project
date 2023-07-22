from django.contrib import admin
from  .models import Product
from import_export.admin import ImportExportModelAdmin
# Register your models here.



class subscription_admin(ImportExportModelAdmin):
    # list_display = ('subscriptionName','weeklySession','numberOfWeek','sessionTime')
    # list_filter = ('subscriptionName','weeklySession','numberOfWeek','sessionTime')
    # search_fields=('subscriptionName','weeklySession','numberOfWeek','sessionTime')
    class Meta:
        model = Product
 
admin.site.register(Product,subscription_admin)