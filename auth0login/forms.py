from django import forms
from django.utils.translation import gettext_lazy as _

from groups.models import Topics

class TopicForm(forms.ModelForm):
	class Meta:
		model = Topics
		fields = ['name']
