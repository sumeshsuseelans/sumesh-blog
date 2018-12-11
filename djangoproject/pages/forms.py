from django import forms
from .models import List
from .models import Books
from .models import MoviesList

class ListForm(forms.ModelForm):
	class Meta:
		model = List
		fields= ["item", "completed"]

class BookForm(forms.ModelForm):
	class Meta:
		model = Books
		fields= ["comment"]

class MoviesListForm(forms.ModelForm):
	class Meta:
		model = MoviesList
		fields= ["MovieName","MovieGener","MovieLanguage","MovieImage"]


