from django import forms

class QuestionForm(forms.Form):
    json_data = forms.CharField(label='JSON Data', widget=forms.Textarea)
    question = forms.CharField(label='Question', max_length=200)
    
