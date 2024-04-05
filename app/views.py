from django.shortcuts import render
import numpy as np

def home(request):

    # create context dictionary
    context = {}

    if request.method == 'POST':
        # Retrieve numbers from the form
        context['x'] = float(request.POST.get('x', 0.0))
        context['out'] = np.full(10, context['x']).sum()

    return render(request, 'app/home.html', context)

