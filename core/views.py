from django.shortcuts import render
from .forms import XDSoftDateTimePickerInput


def date_view(request):
    form = XDSoftDateTimePickerInput()
    return render(request, 'pick.html', {'form':form})


