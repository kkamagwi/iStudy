from django.shortcuts import render
from .forms import StudentForm
from .models import Student


def students_list(request):
    students = Student.objects.all()
    return render(request, 'students/students.html', {'students': students})


def new_student(request):
    form = StudentForm(request.POST)
    if form.is_valid():
        student = form.save(commit=False)
        student.save()
    return render(request, 'students/new_student.html', {'form': form})
