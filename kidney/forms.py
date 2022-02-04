from django import forms



class InputForm(forms.Form):
   
    Age = forms.IntegerField()
    BP  = forms.DecimalField() 
    AL  = forms.DecimalField() 
    PCC = forms.DecimalField()
    BGR= forms.DecimalField() 
    BU = forms.DecimalField() 
    SC = forms.DecimalField() 
    HEMO = forms.DecimalField() 
    PCV = forms.DecimalField() 
    HTN = forms.DecimalField() 
    DM  = forms.DecimalField() 
    Appet = forms.DecimalField()