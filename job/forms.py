from user.models import Profile
from django import forms
from job.models import Job, Company


class JobForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop("request")
        super ().__init__(*args,**kwargs)
        self.fields['company'].queryset = Company.objects.filter(profile=self.request.user.profile)

    class Meta:
        model = Job
        fields = '__all__'
        exclude = ('slug', )

        widgets = {
            'job_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'vacancy': forms.TextInput(attrs={'class': 'form-control'}),
            'max_salary': forms.TextInput(attrs={'class': 'form-control'}),
            'min_salary': forms.TextInput(attrs={'class': 'form-control'}),
            'last_date': forms.TextInput(attrs={'class': 'form-control'}),
        }
    
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ('profile', )

        widgets = {
            'company_name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'web': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }