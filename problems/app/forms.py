from django import forms
from app.models import Review

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['user', 'rating', 'comment']
        widgets = {
            'rating' : forms.NumberInput(attrs={'min': 1, 'max': 5}),
            }