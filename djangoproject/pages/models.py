from django.db import models

class List(models.Model):
	item = models.CharField(max_length=200)
	completed = models.BooleanField(default=False)

	def  __str__(self):
		return self.item

class Books(models.Model):
	comment = models.CharField(max_length=400)

	def  __str__(self):
		return self.comment

class MoviesList(models.Model):
	MovieName = models.CharField(max_length=200)
	MovieGener = models.CharField(max_length=400)
	MovieLanguage = models.CharField(max_length=400)
	MovieImage = models.CharField(max_length=800)

	def  __str__(self):
		return self.MovieName

