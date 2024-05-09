from django.shortcuts import render, redirect
from .models import Pic
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .forms import CreatePicForm

def index(request):
    pics = Pic.objects.all()
    return render(request, "Gallery/index.html", {
        "pics": pics
    })

def pic(request, id):
    pic = Pic.objects.get(pk=id)
    return render(request, "Gallery/pic.html", {
        "pic": pic
    })

def delete_pic(request, id):
    pic = Pic.objects.get(pk=id)
    if pic:
        pic.delete()
        return redirect(reverse("Gallery:home"))
    else:
        return redirect(reverse("Gallery:home"))

class CreatePic(CreateView):
    model = Pic
    form_class = CreatePicForm
    template_name = "Gallery/create.html"
    success_url = reverse_lazy("Gallery:home")
