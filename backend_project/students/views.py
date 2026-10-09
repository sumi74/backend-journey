
from django.shortcuts import render, redirect
from .models import Student
from .forms import StudentForm


def home(request):
    students = Student.objects.all()
    return render(request, "students/home.html", {"students": students})


def add_student(request):
    if request.method == "POST":
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = StudentForm()

    return render(request, "students/add_student.html", {"form": form})


