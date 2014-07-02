from django.shortcuts import render
from django.http import HttpResponse
from schedule.models import Teacher



# this displays all the teachers
def teacher(request):
	all_teachers = Teacher.objects.all()
	return render(request, 'teacher.html', {'all_teachers':all_teachers})

