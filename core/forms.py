from django import forms
from .models import Todo


class TodoForm(forms.ModelForm):
	class Meta:
		model = Todo
		fields = '__all__'

		widgets = {
			'event_date':forms.TextInput(attrs={'type':'date'}),
			'event_time':forms.TextInput(attrs={'type':'time'}),
		}

		labels = {
			'note': 'Todo'
		}


class SearchForm(forms.Form):
	search = forms.CharField(max_length=100)