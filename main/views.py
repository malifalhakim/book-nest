from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'M.Alif Al Hakim',
        'class': 'PBP C'
    }

    return render(request, "main.html", context)