from django.forms import ModelForm
from django import forms
from .models import Task
class TaskForm(ModelForm):
	title=forms.CharField(max_length=100)
	title.widget.attrs.update({'style':'color:#4C2719;  border=3px solid black; width:500px; font-size:24px; padding:10px; background:#EDE580;'})
	completed=forms.BooleanField()
	completed.widget.attrs.update({'style':'width:50px; height:20px; background:#EDE580;'})
	class Meta :
		model=Task
		fields=['title','completed']
