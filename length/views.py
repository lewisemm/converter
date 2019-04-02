from django.shortcuts import render

from length.forms import LengthConverterForm

convert_to_metre = {
    "centimetre": 0.01,
    "metre": 1.0,
    "mile": 1609.34
}
convert_from_metre = {
    "centimetre": 100,
    "metre": 1.0,
    "mile": 0.000621371
}

# Create your views here.
def convert(request):
    form = LengthConverterForm()
    if request.GET:
        input_unit = request.GET['input_unit']
        input_value = request.GET['input_value']
        output_unit = request.GET['output_unit']
        metres = convert_to_metre[input_unit] * float(input_value)
        output_value = metres * convert_from_metre[output_unit]
        data = {
            "input_unit": input_unit,
            "input_value": input_value,
            "output_unit": output_unit,
            "output_value": round(output_value, 3)
        }
        form = LengthConverterForm(initial=data)
        return render(
            request, "length.html", context={"form": form})
    return render(
        request, "length.html", context={"form": form})