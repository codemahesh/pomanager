from unicodedata import category
from urllib import request
from django import forms
from .models import Customer, CustomerPo, Uom 
from django.core import validators



class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = '__all__'
        labels = {
            'customer_name': 'Customer Name',
            'customer_code': 'Customer Code'
        }  
#### unkow for defalt selct caleut not worki9ng
    def __init__(self, *args, **kwargs):
        super(CustomerForm, self).__init__(*args, **kwargs)
        self.fields['category'].empty_label = "Select"
        self.fields['place'].required = False


class CustomerRegistration(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ['customer_name','customer_code','category','address','place']
        widgets = {
            'customer_name': forms.TextInput(attrs={'class':'form-control'}),
            'customer_code': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(attrs={'class':'form-select'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'place': forms.TextInput(attrs={'class':'form-control'}),
        }


class UomForm(forms.ModelForm):
    class Meta:
        model = Uom
        fields = ['unit','unit_type','unit_code']
        widgets = {
            'unit': forms.TextInput(attrs={'class':'form-control'}),
            'unit_type': forms.TextInput(attrs={'class':'form-control'}),
            'unit_code': forms.TextInput(attrs={'class':'form-control'}),

        }

class CustomerPoForm(forms.ModelForm):
 
    class Meta:
        model = CustomerPo
        fields =['customer_po_number','date','customer_name','status']
        widgets = {
            'customer_po_number': forms.TextInput(attrs={'class':'form-control',}),
            'date': forms.DateInput(attrs={'class':'form-control','id':'datepicker','placeholder':'yyyy-mm-dd','autocomplete': 'off'}),
            'customer_name': forms.Select(attrs={'class':'form-select'}),
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['customer_name'].queryset = Customer.objects.none()

        if 'customer_name' in self.data:
            try:
                customer_name = self.data.get('customer_name')
                self.fields['customer_name'].queryset = Customer.objects.filter(customer_name=customer_name).order_by('customer_name')
            except(ValueError, TypeError):
                pass
