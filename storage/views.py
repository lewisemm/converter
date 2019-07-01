from django.shortcuts import render

from .forms import StorageConverterForm

convert_to_gb = {
    "mb": 0.0009765625,
    "gb": 1.0,
    "tb": 1024
}
convert_from_gb = {
    "mb": 1024.0,
    "gb": 1.0,
    "tb": 0.0009765625
}
# Create your views here.
def storage(request):
    form = StorageConverterForm()
    if request.GET:
        input_unit = request.GET['input_unit']
        input_value = request.GET['input_value']
        output_unit = request.GET['output_unit']
        gb = convert_to_gb[input_unit] * float(input_value)
        output_value = gb * convert_from_gb[output_unit]
        data = {
            "input_unit": input_unit,
            "input_value": input_value,
            "output_unit": output_unit,
            "output_value": round(output_value, 3)
        }
        form = StorageConverterForm(initial=data)
        return render(
            request, "storage.html", context={"form": form})
    return render(
        request, "storage.html", context={"form": form})
