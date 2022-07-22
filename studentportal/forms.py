from profiles.models import Apply, CustomUser, Studentdata, Staffdata, Exam
from django import forms
from studentportal.models import TrialUser


class Studentproform(forms.ModelForm):
    class Meta:
        model = Studentdata
        fields = ['firstname', 'lastname', 'email', 'phone', 'state', 'study_field', 'student_class', 'class_form', 'student_image']


class Staffproform(forms.ModelForm):
    class Meta:
        model = Staffdata
        fields = '__all__'        
        exclude =['nickname', 'slug']

class Applyform(forms.ModelForm):
    class Meta:
        model = Apply
        fields = '__all__'  
        exclude = ['nickname', 'slug']      
        

class Register(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password','first_name', 'last_name', 'email', 'state', 'phone', 'country', 'mailing_address']

class Examform(forms.ModelForm):
    class Meta:
        model = Exam
        fields = ['course', 'student', 'student_username', 'scores']
        
