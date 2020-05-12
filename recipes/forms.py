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
""""
# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name
    def url(self):
        return f"/author/{self.id}"



class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return self.title
    def url(self):
        


"""
