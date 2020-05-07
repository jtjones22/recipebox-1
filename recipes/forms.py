from django import forms
from recipes.models import Author


class AddRecipeForm(forms.Form):
	title = forms.CharField(max_length=30)
	description = forms.CharField(widget=forms.Textarea)
	time_required = forms.CharField(max_length=50)
	instructions = forms.CharField(widget=forms.Textarea)
	author = forms.ModelChoiceField(queryset=Author.objects.all())


class AddAuthorForm(forms.ModelForm):
	class Meta:
		model = Author
		fields = [
			'name',
			'bio',
		]


class LoginForm(forms.Form):
	username = forms.CharField(max_length=50)
	password = forms.CharField(widget=forms.PasswordInput)


class CreateNewUserForm(forms.Form):
