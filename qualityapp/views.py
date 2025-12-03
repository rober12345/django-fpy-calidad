from django import forms
from django.shortcuts import render

class InspectorFPYForm(forms.Form):
    # Inspector 1
    inspector1_name = forms.CharField(label="Inspector 1", max_length=50)
    inspector1_inspected = forms.IntegerField(label="Inspeccionadas 1", min_value=0)
    inspector1_reworked = forms.IntegerField(label="Retrabajadas 1", min_value=0)

    # Inspector 2
    inspector2_name = forms.CharField(label="Inspector 2", max_length=50)
    inspector2_inspected = forms.IntegerField(label="Inspeccionadas 2", min_value=0)
    inspector2_reworked = forms.IntegerField(label="Retrabajadas 2", min_value=0)

    # Inspector 3
    inspector3_name = forms.CharField(label="Inspector 3", max_length=50)
    inspector3_inspected = forms.IntegerField(label="Inspeccionadas 3", min_value=0)
    inspector3_reworked = forms.IntegerField(label="Retrabajadas 3", min_value=0)

    # Inspector 4
    inspector4_name = forms.CharField(label="Inspector 4", max_length=50)
    inspector4_inspected = forms.IntegerField(label="Inspeccionadas 4", min_value=0)
    inspector4_reworked = forms.IntegerField(label="Retrabajadas 4", min_value=0)


def inspector_fpy_view(request):
    results = None
    chart_labels = []
    chart_fpy = []
    chart_inspected = []
    chart_reworked = []

    if request.method == "POST":
        form = InspectorFPYForm(request.POST)
        if form.is_valid():
            results = []
            for i in range(1, 4 + 1):
                name = form.cleaned_data[f"inspector{i}_name"]
                inspected = form.cleaned_data[f"inspector{i}_inspected"]
                reworked = form.cleaned_data[f"inspector{i}_reworked"]

                if inspected > 0:
                    fpy = (inspected - reworked) / inspected * 100
                else:
                    fpy = 0

                fpy_rounded = round(fpy, 2)

                results.append({
                    "name": name,
                    "inspected": inspected,
                    "reworked": reworked,
                    "fpy": fpy_rounded,
                })

                chart_labels.append(name)
                chart_fpy.append(fpy_rounded)
                chart_inspected.append(inspected)
                chart_reworked.append(reworked)
    else:
        form = InspectorFPYForm()

    context = {
        "form": form,
        "results": results,
        "chart_labels": chart_labels,
        "chart_fpy": chart_fpy,
        "chart_inspected": chart_inspected,
        "chart_reworked": chart_reworked,
    }
    return render(request, "qualityapp/inspectors_fpy.html", context)