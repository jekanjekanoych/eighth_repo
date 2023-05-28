from django.shortcuts import render
from student.forms import StudentForm


def index(request):
    if request.method == "GET":
        form = StudentForm()
        return render(request, "index.html", {"form": form})
    form = StudentForm(request.POST)
    if form.is_valid():
        form.save()
    return render(request, "index.html", {"form": form})
