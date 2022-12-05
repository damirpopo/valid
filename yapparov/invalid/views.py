from django.shortcuts import render
from .forms import userreg
from django.http import HttpResponse

def index(request):
    if request.method == "POST":
        user = userreg(request.POST)
        if user.is_valid():
            return HttpResponse("Вы успешно зарегистрировались")
        else:
            return HttpResponse("invalid")
    else:
        return render(request,"index.html", {"form": userreg})


def inflex(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("password")
        if name == "User1" and password == "12345678":
            return HttpResponse("вы успешно вошли")
        else:
            return HttpResponse("неверные данные")
    else:
        form = userreg()
        return render(request, "inflex.html", {"form": form})



