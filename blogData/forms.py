from django import forms
from .models import Author, Tag, Comment

class AuthorForm(forms.Form):
    first_name = forms.CharField(label="Nombre", max_length=50)
    last_name = forms.CharField(label="Apellidos", max_length=50)
    email_address = forms.EmailField(label="Email")


class PostForm(forms.Form):
    title = forms.CharField(label="Título", max_length=100)
    excerpt = forms.CharField(label="Resumen", max_length=200)
    image = forms.ImageField(
        label="Imagen",
        required=False,
        widget=forms.ClearableFileInput(attrs={
            "accept": "image/*",
        })
    )
    content = forms.CharField(
        label="Contenido",
        widget=forms.Textarea(attrs={"rows": 5})
    )

    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

class CommentForm(forms.Form):
    name = forms.CharField(label="Nombre", max_length=50)
    email = forms.EmailField(label="Email")
    text = forms.CharField(label="Comentario", widget=forms.Textarea(attrs={"rows": 5}))
