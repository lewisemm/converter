from django import forms

class LengthConverterForm(forms.Form):
    MEASUREMENTS = (
        ('centimetre', 'Centimetre'),
        ('metre', 'Metre'),
        ('mile', 'Mile'),
        ('inch', 'Inch'),
        ('kilometre', 'Kilometre'),
        ('yard', 'Yard'),
        ('millimetre', 'Millimetre'),
        ('foot', 'Foot')
    )
    input_unit = forms.ChoiceField(choices=MEASUREMENTS)
    input_value = forms.DecimalField(decimal_places=3)
    output_unit = forms.ChoiceField(choices=MEASUREMENTS)
    output_value = forms.DecimalField(decimal_places=3, required=False)