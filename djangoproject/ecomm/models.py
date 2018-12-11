from django.db import models

class Items(models.Model):
	item = models.CharField(max_length=800)
	Description = models.CharField(max_length=800)
	ItemImage = models.CharField(max_length=800)
	
	def  __str__(self):
		return self.item
