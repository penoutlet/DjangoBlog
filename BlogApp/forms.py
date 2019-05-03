from django import forms
from BlogApp.models import Post,Comment
from django.utils import timezone
class PostForm(forms.ModelForm):

	class Meta():
		model = Post
		fields = ('author','title','text')

		widgets = {
			'title':forms.TextInput(attrs={'class':'textinputclass'}),
			'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})

		}		

class CommentForm(forms.ModelForm):

	class Meta():
		model = Comment
		fields = ('author','text')

		widgets = {
			'author':forms.TextInput(attrs={'class':'textinputclass'}),
			'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'}),
			# 'create_date': forms.DateTimeField()
		}
