from django import forms

SEX_CHOICES= [
    (1, 'Male'),
    (0, 'Female')
    ]

class InputForm(forms.Form):
   
    Age = forms.IntegerField()
    Sex = forms.ChoiceField(choices=SEX_CHOICES, required=True)
    Total_Bilirubin = forms.DecimalField()
    Direct_Bilirubin  = forms.DecimalField()
    Alkaline_Phosphotase = forms.DecimalField()
    Alamine_Aminotransferase = forms.DecimalField()
    Aspartate_Aminotransferase = forms.DecimalField()
    Total_Protiens = forms.DecimalField()
    Albumin= forms.DecimalField()
    Albumin_and_Globulin_Ratio = forms.DecimalField()