from django.db import models

from django.contrib.auth.hashers import check_password
# Create your models here.



class Person(models.Model):
    first_name = models.CharField(max_length=20,help_text='Enter your first name')
    second_name = models.CharField(max_length=20,help_text='Enter your first name')
    age = models.IntegerField()
    email = models.EmailField()
    phone = models.IntegerField(help_text='Enter your phone')
    password = models.TextField(max_length=50)
    block_student = models.BooleanField(default=0)
    attended_lectures = models.IntegerField(default=0)
    AreYouStudent = models.BooleanField(default=1)

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.email

class Course(models.Model):
    course_id = models.AutoField(primary_key=True)
    course_name = models.CharField(max_length=50,help_text='Enter Course Name')
    description = models.TextField(max_length=200,help_text='Enter Course description')

    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)."""
        return self.course_name


class RegisteredCourses(models.Model):
    registered_course = models.ManyToManyField(Course)
    registered_student = models.ManyToManyField(Person,related_name='registerAstudent')
    registered_Teacher = models.ManyToManyField(Person,related_name='registerAteacher')
    number_of_students_registered = models.IntegerField(null=True)



