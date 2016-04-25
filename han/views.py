from django.shortcuts import render
from .models import contents

# Create your views here.
def main_page(request):
    if request.method == "POST":
        pass

    return render(request, 'main_page.html')

def agree_page(request):
    return render(request, 'agree_page.html')

def edit_page(request):
    pass
