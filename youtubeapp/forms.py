from .models import Comment
from django import forms

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields =('name','message','channel',)
        exclude =('channel',)
        labels = {
            'name':'名前',
            'message':'コメント'
            }