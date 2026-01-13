from django import forms
from .models import Employee
import re

email_regex = r'^[a-zA-Z0-9._]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,7}$'

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        widgets = {
            'emp_DOJ': forms.DateInput(attrs={'type': 'date'}),
            'emp_address': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(EmployeeForm, self).__init__(*args, **kwargs)
        for name, field in self.fields.items():
            field.required = True
            classes = field.widget.attrs.get('class', '')
            if 'form-control' not in classes:
                field.widget.attrs['class'] = (classes + 'form-control').strip()

    def clean_emp_email(self):
        emp_email = self.cleaned_data.get('emp_email')
        if not re.match(email_regex, emp_email):
            raise forms.ValidationError("Invalid email format")
        return emp_email
    def clean_emp_ph(self):
        emp_ph = self.cleaned_data.get('emp_ph')
        if len(str(emp_ph)) != 10 or not str(emp_ph).isdigit():
            raise forms.ValidationError("Phone number must be 10 digits")
        return emp_ph
    def clean_empname(self):
        empname = self.cleaned_data.get('empname')
        if not empname.replace(" ", "").isalpha():
            raise forms.ValidationError("Name must contain only alphabetic characters and spaces")
        return empname
    def clean_empid(self):
        empid = self.cleaned_data.get('empid')
        if len(str(empid)) != 4 or not str(empid).isdigit():
            raise forms.ValidationError("Employee ID must be a 4-digit number")
        return empid
    def clean_emp_sal(self):
        emp_sal = self.cleaned_data.get('emp_sal')
        if emp_sal <= 0 or not str(emp_sal).isdigit():
            raise forms.ValidationError("Salary must be a positive number")
        return emp_sal