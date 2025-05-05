from django.contrib import admin

from users.models import Student, Teacher, Group, Admin, Branch, Course, Methodist, Instructor, CustomUser

# Register your models here.
admin.site.register(Student)
admin.site.register(Teacher)
admin.site.register(Group)
admin.site.register(Branch)
admin.site.register(Admin)
admin.site.register(Course)