from django.contrib import admin

from .models import Item, Transaction


class ItemAdmin(admin.ModelAdmin):
	list_display = ('name', 'current_stock', 'price', )

class TransactionAdmin(admin.ModelAdmin):
	list_display = ('item', 'timestamp' )

admin.site.register(Item, ItemAdmin)
admin.site.register(Transaction, TransactionAdmin)
# Register your models here.
