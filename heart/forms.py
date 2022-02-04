from django import forms

SEX_CHOICES= [
    (1, 'Male'),
    (0, 'Female')
    ]

class InputForm(forms.Form):
   
    Age = forms.IntegerField()
    Sex = forms.ChoiceField(choices=SEX_CHOICES, required=True)
    Chest_pain_type = forms.IntegerField()
    Trestbps = forms.IntegerField()
    Serum_cholesterol_in_mg_dl = forms.IntegerField()
    Restecg = forms.IntegerField() 
    Thalach = forms.IntegerField() 
    Exang = forms.IntegerField() 
    Oldpeak = forms.IntegerField()
    Slope = forms.IntegerField()
    Thal = forms.IntegerField()
