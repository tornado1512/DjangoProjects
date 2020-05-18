from django import forms
class VideoForm(forms.Form):
    videoName=forms.CharField(max_length=20,
        widget=forms.TextInput(attrs={
        'class':'form-control',
        'id':'inputName',
        'placeholder':'name'}))

    videoDesc=forms.CharField(widget=forms.Textarea({
        'class':'form-control',
        'id':'comment',
        'row':'5',
        'placeholder':'comment'

    }))
