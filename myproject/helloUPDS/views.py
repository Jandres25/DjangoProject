from django.shortcuts import render

# Create your views here.
def helloUPDS(request):
    return render(request, 'helloUPDS.html', {})

