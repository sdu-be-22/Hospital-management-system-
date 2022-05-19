from django import forms

from .models import Comment

class CommentForm(forms.ModelForm):
	body = forms.CharField(widget=forms.Textarea(attrs={
			'rows': 10,
		}))
	class Meta:
		model = Comment
		fields = ['username', 'body']
