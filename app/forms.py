from django import forms
from .models import PatientEnroll


class PatientForm(forms.ModelForm):

    class Meta :
        model = PatientEnroll
        fields = '__all__'

    def clean_email(self):
        return self.cleaned_data['email'].lower()

    def __init__(self, *args, **kwargs):
        super(PatientForm, self).__init__(*args, **kwargs)
        self.fields['name'].label = "Name"
        self.fields['email'].label = "Email"
        self.fields['age'].label = "Age"
        self.fields['gender'].label = "Gender"
        self.fields['preg'].label = ""
