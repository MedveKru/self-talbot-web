from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from config import picture_name, picture_front_name, z_indent
from talbot import get_perspective, get_front

from .forms import TalbotProcess


def render_talbot(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = TalbotProcess(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            get_perspective(wavelength=form.cleaned_data['wavelength'],
                            period=form.cleaned_data['period'], phase_shift=form.cleaned_data['phase_shift'],
                            show_z_talbot=form.cleaned_data['show_z_talbot'])
            get_front(z_indent=form.cleaned_data['z_indent'])
        print(form)

    # if a GET (or any other method) we'll create a blank form
    else:
        form = TalbotProcess()

    return render(request, 'index.html', {'form': form})


def index(request):
    get_perspective()
    get_front(z_indent)
    return render(request, 'index.html', {"side": picture_name, "front": picture_front_name})
