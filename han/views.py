from django.shortcuts import render
from django.shortcuts import redirect
from .models import contents

# Create your views here.
def main_page(request):
    if request.method == "POST":
        pass

    return render(request, 'main_page.html')

def agree_page(request):
    if request.method =="POST":

        pass



    return render(request, 'agree_page.html')


def edit_page(request):
    if request.method == "POST":
        new_contents = contents(
            summary = request.POST.get('summary'),
            workexp = request.POST.get('work_exp'),
        )
        new_contents = request.user
        new_contents.save()

        return redirect(select_template)


    return render(request,'edit_page.html')

def select_template(request):
    new_contents = contents.objects.get(id==1)

    ctx={
        'contents' : new_contents,
    }

    return render(request, 'select_template.html',ctx)

