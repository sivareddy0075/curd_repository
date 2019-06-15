from django import forms

class InsertDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Product ID',
                'class':'form-control'
            }
        )
    )
    product_name = forms.CharField(
        label="Enter Your product Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Product Name',
                'class':'form-control'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Your Product Cost",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Your Product Cost',
                'class':'form-control'
            }
        )
    )
    product_color = forms.CharField(
        label="Enter Your Product Color",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Product Color',
                'class':'form-control'
            }
        )
    )
    product_class = forms.CharField(
        label="Enter Your Product Class",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Product Class',
                'class':'form-control'
            }
        )
    )
    customer_name = forms.CharField(
        label="Enter Customer Name",
        widget=forms.TextInput(
            attrs={
                'placeholder':'Customer Name',
                'class':'form-control'
            }
        )
    )
    customer_mobile = forms.IntegerField(
        label="Enter Customer Mobile",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Customer Mobile',
                'class':'form-control'
            }
        )
    )
    customer_email = forms.EmailField(
        label="Enter Customer Email",
        widget=forms.EmailInput(
            attrs={
                'placeholder':'Customer Email',
                'class':'form-control'
            }
        )
    )




class UpdateDataForm(forms.Form):
    product_id = forms.IntegerField(
        label= "Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'placeholder':'Product ID',
                'class':'form-control'
            }
        )
    )
    product_cost = forms.IntegerField(
        label="Enter Your Product Cost",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Your Product Cost',
                'class': 'form-control'
            }
        )
    )





class DeleteDataForm(forms.Form):
    product_id = forms.IntegerField(
        label="Enter Product ID",
        widget=forms.NumberInput(
            attrs={
                'placeholder': 'Product ID',
                'class': 'form-control'
            }
        )
    )

