from django.db import models

# Create your models here.
class Teacher(models.Model):
	teacher_id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=140)
	last_name = models.CharField(max_length=140)
	email = models.CharField(max_length=140)
	address = models.CharField(max_length=140)
	city = models.CharField(max_length=140)
	phone_number = models.CharField(max_length=140)

class Student(models.Model):
	studend_id = models.IntegerField(primary_key=True)
	first_name = models.CharField(max_length=140)
	last_name = models.CharField(max_length=140)
	email = models.CharField(max_length=140)
	address = models.CharField(max_length=140)

class Course(models.Model):
	class_id = models.IntegerField(primary_key=True)
	subject = models.CharField(max_length=140)
	section = models.CharField(max_length=140)
	content = models.CharField(max_length=140)


class Entry(models.Model):
	student = models.ForeignKey(Student)
	teacher = models.ForeignKey(Teacher)
	course = models.ForeignKey(Course)

class Schedule(models.Model):
	Schedule = models.ManyToManyField(Entry)