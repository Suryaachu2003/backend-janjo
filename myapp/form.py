from django import forms
from .models import student, teacher

class studentform(forms.Form):
    name=forms.CharField(max_length=50)
    age=forms.IntegerField()
    email=forms.EmailField()
    gender=forms.CharField(widget=forms.RadioSelect(choices=[('M','Male'),('F','Female'),('O','Other')]))
    file=forms.FileField()
    
    def clean(self) ->dict[str,any]:
        cleaned_data=super().clean()
        name=cleaned_data.get('name')
        age=cleaned_data.get('age')
        email=cleaned_data.get('email')
        
        if name.isupper():
            self.add_error('name',"name should not be in uppercase")
        if age<18:
            self.add_error('age',"age should be greater than 18")
        if email and not email.endswith('@gmail.com'):
            self.add_error('email',"email should be in gmail")
        return cleaned_data

class TeacherForm(forms.ModelForm):
    class Meta:
        model=teacher
        fields='__all__'

class JobApplicationForm(forms.Form):
    name = forms.CharField(max_length=100)
    email = forms.EmailField()
    phone = forms.CharField(max_length=20)
    cover_letter = forms.CharField(widget=forms.Textarea)
    resume = forms.FileField()  
    
    
class loginform(forms.Form):
    username=forms.CharField(max_length=50)
    password=forms.CharField(widget=forms.PasswordInput)