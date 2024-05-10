from django.shortcuts import render, redirect
from .models import Pic
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from .forms import CreatePicForm
from django.contrib import messages

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

    if request.user.is_authenticated:
        if request.user.is_superuser:
            pic.delete()
            return redirect(reverse("Gallery:home"))
        elif (request.user ==  pic.author):
            pic.delete()
            return redirect(reverse("Gallery:home"))
        else:
            messages.error(request, "My nigga, you cannot delete an image if you're not the author, or, you're not the superuser ;)")
            return redirect(reverse("Gallery:home"))
    else:
        messages.error(request, "You need to be logged in to delete a Pic")
        return redirect(reverse("Accounts:login"))

def create_pic(request):
    if request.method == "POST":
        if request.user.is_authenticated:
            form = CreatePicForm(request.POST, request.FILES)
            if form.is_valid():
                pic = form.save(commit=False)
                pic.author = request.user
                pic.save()
                return redirect(reverse("Gallery:home"))
    else:
        form = CreatePicForm()

    return render(request ,"Gallery/create.html", { "form": form })