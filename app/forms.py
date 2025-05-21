from django import forms

from app.models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ('user',)

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.visible_fields():
            field.field.widget.attrs['class'] = 'form-control'
