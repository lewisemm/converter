from django import forms

class StorageConverterForm(forms.Form):
    MEASUREMENTS = (
        ('mb', 'MB'),
        ('gb', 'GB'),
        ('tb', 'TB'),
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    input_value = forms.DecimalField(decimal_places=3)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_value = forms.DecimalField(decimal_places=3, required=False)