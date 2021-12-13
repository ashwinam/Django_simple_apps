from django import forms
from .models import Student, MasterData, Mark_Attendence

class StudentForm(forms.Form):
    ID = forms.CharField(max_length=100, label='Student ID')
    name = forms.CharField(max_length=100, label='Student Name')
    email = forms.CharField(max_length=100, label='Student Email')
    Class = forms.CharField(max_length=100, label='Student Class')

    def clean_name(self):
        valname = self.cleaned_data['name']
        if len(valname) < 4:
            raise forms.ValidationError("Enter more than or equal to 4")
        return valname

class StudentModelForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__' # or you can use List also with specific fields name.


class MasterDataForm(forms.ModelForm):
    class Meta:
        model = MasterData
        fields = ['st_id', 'st_name', 'st_mail', 'subject']

class MarkAttendenceForm(forms.ModelForm):
    class Meta:
        model = Mark_Attendence
        fields = ['ID', 'subject_name']

class oneForm(forms.Form):
    ID = forms.IntegerField()

    
