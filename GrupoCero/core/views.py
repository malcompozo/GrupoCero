from django.shortcuts import render

# index
def index(request):
    return render(request,"core/index.html")

# panel
def panel(request):
    return render(request,"core/panel.html")



