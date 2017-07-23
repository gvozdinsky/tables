from django import forms
from .models import Product, Company, Warehouse, Client, Order, OrderProductsList, Service, OrderServicesList
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from djangoformsetjs.utils import formset_media_js



class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ['name', 'vendor_code', 'barcode', 'unit','description']



class ServiceForm(forms.ModelForm):
    
    class Meta:
        model = Service
        fields = ['name', 'description']




class EmployeeForm(UserCreationForm):
    # add_product = forms.BooleanField()
    # change_product = forms.BooleanField()
    # delete_product = forms.BooleanField()

    class Meta:
        model = User
        fields = ['username','first_name','last_name', 'email', 'password1', 'password2']


class EmployeeEditForm(forms.ModelForm):
    # add_product = forms.BooleanField()
    # change_product = forms.BooleanField()
    # delete_product = forms.BooleanField()

    class Meta:
        model = User
        fields = ['first_name','last_name', 'email']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['name', 'legal_address', 'actual_address', 'telephone_number','email','website','description']


class WarehouseForm(forms.ModelForm):
    class Meta:
        model = Warehouse
        fields = ['name', 'address']

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = ['name', 'address', 'telephone_number', 'description']


class OrderForm(forms.ModelForm):
    client = forms.ModelChoiceField(queryset=Client.objects.none(), label='Клиент')

    class Meta:
        model = Order
        fields = ['client', 'urgency', 'comment']

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('client_qs')
        super(OrderForm, self).__init__(*args,**kwargs)
        self.fields['client'].queryset = qs

class OrderProductsListForm(forms.ModelForm):
    product = forms.ModelChoiceField(queryset=Product.objects.none(), label='Товар', required=True)

    class Meta:
        fields = ['product', 'quantity']
        model = OrderProductsList


    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('product_qs')
        super(OrderProductsListForm, self).__init__(*args, **kwargs)
        self.fields['product'].queryset = qs


class OrderServicesListForm(forms.ModelForm):
    service = forms.ModelChoiceField(queryset=Service.objects.none(), label='Услуга', required=True)

    class Meta:
        fields = ['service']

    def __init__(self, *args, **kwargs):
        qs = kwargs.pop('service_qs')
        super(OrderServicesListForm, self).__init__(*args, **kwargs)
        self.fields['service'].queryset = qs




