from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse

from datetime import datetime

from .models import Item, Transaction

class SellingView(View):
	def get(self, request, **kwargs):
		barcode = request.GET.get('code')
		item = Item.objects.get(barcode=barcode)
		item.current_stock = item.current_stock - 1
		item.save()

		Transaction.objects.create(
			item=item,
			timestamp=datetime.now()
		)
		return HttpResponse()
# Create your views here.
