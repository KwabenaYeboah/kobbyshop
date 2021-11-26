from django import forms

PRODUCT_QUANTITY_CHOICES = [(item, str(item)) for item in range(1,21)]

class AddProductToCartForm(forms.Form):
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES, coerce=int)
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)
    