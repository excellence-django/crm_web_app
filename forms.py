from django import forms
from studentapp.models import Student,Course,Enroll
from django.core.exceptions import ValidationError

class Studentform(forms.ModelForm):
    class Meta:
        model=Student
        fields="__all__"

        widgets = {"rollno": forms.NumberInput(attrs={"class": "form-control"}),
                   "name": forms.TextInput(attrs={"class": "form-control"}),
                   "address": forms.TextInput(attrs={"class": "form-control"}),
                   "mobile": forms.NumberInput(attrs={"class": "form-control"}),
                   "email": forms.EmailInput
                   (attrs={"class": "form-control"})}


    def clean(self):
        cleaned_data = super().clean()
        id = cleaned_data.get("id")
        name = cleaned_data.get("name")
        email = cleaned_data.get("email")



class LoginForm(forms.Form):
    username=forms.CharField()
    password=forms.CharField(widget=forms.PasswordInput())

class Courseform(forms.ModelForm):
    class Meta:
        model=Course
        fields="__all__"

        widgets={
                 "name":forms.TextInput(attrs={"class":"form-control"}),
                 "details":forms.TextInput(attrs={"class":"form-control"})
                 }
class MyModelChoiceField(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name
class MyModelChoiceField1(forms.ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.e_id

class Enrollform(forms.ModelForm):
    class Meta:
        model = Enroll
        fields = ('rollno', 'couse_id', 'fees','details')




    rollno =  MyModelChoiceField(queryset=Student.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'blank': 'True'}))
    couse_id = MyModelChoiceField(queryset=Course.objects.all(), widget=forms.Select(attrs={'class': 'form-control', 'blank': 'True'}))
    fees = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    details = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control','rows': 5, 'cols': 50}))

class EnrollSingleform(forms.ModelForm):
        class Meta:
            model = Enroll
            fields = ('e_id',)

        def clean(self):
            cleaned_data = super().clean()
            e_id = cleaned_data.get("e_id")
            status = cleaned_data.get("status")

        CHOICES = [
            ('Paid', 'Paid'),
            ('Not paid', 'Not paid'),
        ]
        e_id = MyModelChoiceField1(queryset=Enroll.objects.all(),
                                    widget=forms.Select(attrs={'class': 'form-control'}))
        details = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}))
        fees = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}))
        student = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}))
        couse = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control','readonly':'readonly'}))
        status = forms.CharField(widget=forms.RadioSelect(attrs={"select":"Paid"},choices=CHOICES))

        # widgets={"e_id":forms.Select(attrs={'class': 'form-control', 'blank': 'True'})}