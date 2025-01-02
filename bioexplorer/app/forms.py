from django import forms

operators = (('+', '+')
             ,('-', '-')
             ,('*', '*')
             ,('/', '/'))

class CalculatorForm(forms.Form):
    num1 = forms.FloatField(label="Number 1")
    operator = forms.ChoiceField(choices=operators, label="Operator")
    num2 = forms.FloatField(label="Number 2")
