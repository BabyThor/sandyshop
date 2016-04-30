from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Item(models.Model):
	name = models.CharField(max_length=200)
	current_stock = models.IntegerField()
	barcode = models.IntegerField()
	price = models.IntegerField()

	def __unicode__(self):
		return '%s : %s' % (self.name, self.price)

class Transaction(models.Model):
	item = models.ForeignKey('stocks.Item')
	timestamp = models.DateTimeField()