from django.contrib import admin

# Register your models here.
from students.models import Person, Course, RegisteredCourses

admin.site.register(Person)
admin.site.register(Course)
admin.site.register(RegisteredCourses)
