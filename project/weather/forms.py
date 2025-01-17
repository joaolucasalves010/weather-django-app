from django import forms

class CityNameForm(forms.Form):
  city_name = forms.CharField(max_length=100, required=True, widget=forms.TextInput(attrs={'placeholder': 'Digite o nome da cidade:','id': 'city_name_input',}))