from django.shortcuts import render, redirect
from schools.forms import SchoolForm
from schools.models import School

def list(request):
    schools = School.objects.all()

    return render(request, "list.html", {'schools': schools})

def add(request):
    if request.method == "POST":
        form = SchoolForm(request.POST)
        if form.is_valid():
            try:
                form.save();
                return redirect("/list")
            except:
                pass
    form = SchoolForm()
    return render(request, "add.html", {'form': form})