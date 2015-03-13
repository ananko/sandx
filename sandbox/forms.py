from django import forms

class NewNoteForm(forms.Form):
    content = forms.CharField(required=True, widget=forms.Textarea)

