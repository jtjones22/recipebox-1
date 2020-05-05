from django import forms
from recipes.models import Author

class RecipeAddForm(forms.Form):
	title = forms.CharField(max_length=30)
	body = forms.CharField(widget=forms.Textarea)
	author = forms.ModelChoiceField(queryset=Author.objects.all())






"""
class Author(models.Model):
    name = models.CharField(max_length=50)
    bio = models.TextField()

    def __str__(self):
        return self.name



class Recipe(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=50)
    instructions = models.TextField()

    def __str__(self):
        return self.title

"""