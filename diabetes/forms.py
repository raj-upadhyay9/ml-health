from django import forms

class InputForm(forms.Form):
    
    Pregnancies = forms.IntegerField()
    Glucose = forms.DecimalField()
    BloodPressure = forms.DecimalField()
    SkinThickness = forms.DecimalField()
    Insulin= forms.DecimalField()
    BMI = forms.DecimalField()
    DiabetesPedigreeFunction = forms.DecimalField()
    Age= forms.IntegerField()
