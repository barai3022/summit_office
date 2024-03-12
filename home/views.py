from django.shortcuts import render

# Create your views here.
def home(request):
    template_path = "home/index.html"

    title = "Welcome to Summit Power Limited"

    x = {}
    x["title"] = title

    context = {
        "x":x
    }

    return render(request, template_path, context) 