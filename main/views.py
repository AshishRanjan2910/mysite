from django.http import HttpResponseRedirect
from django.shortcuts import render
from .models import ToDoList, Item
from .forms import CreateNewList


# Create your views here.
def index(response, id):
    list_prop = ToDoList.objects.get(id=id)

    if response.method == "POST":
        if response.POST.get("save"):
            for item in list_prop.item_set.all():
                if response.POST.get("c"+str(item.id)) == "clicked":
                    item.completed = True
                else:
                    item.completed = False
                item.save()
        elif response.POST.get("newItem"):
            task = response.POST.get("new")
            if len(task) > 2:
                list_prop.item_set.create(task=task, completed=False)
            else:
                print("--invalid--")

    return render(response, "main/lists.html", {"ln": list_prop})


def home(response):
    return render(response, "main/home.html", {})


def create(response):
    if response.method == "POST":
        # Catching the request body and decrypting it out using cleaned_data
        form = CreateNewList(response.POST)
        if form.is_valid():
            name = form.cleaned_data["name"]
            t = ToDoList(name=name)
            t.save()
        return HttpResponseRedirect("/%i" % t.id)
    else:
        form = CreateNewList()

    return render(response, "main/create.html", {"form": form})
