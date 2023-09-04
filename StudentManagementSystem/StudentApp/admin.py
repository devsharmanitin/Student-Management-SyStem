from .models import *
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin


# Register your models here.
class CustomUserAdmin(UserAdmin):
    list_display = ['username' , 'user_type']
    
    # fieldsets = (
    #     ('UserType',{'fields':('user_type','date_joined',)}),
    # )
    
admin.site.register(Course)
admin.site.register(Session) 
admin.site.register(Student)
admin.site.register(CustomUser , CustomUserAdmin)
admin.site.register(Staff)
admin.site.register(Subject)
admin.site.register(StaffNotification)
admin.site.register(StaffLeave)
admin.site.register(StaffFeedback)
admin.site.register(StudentNotification)
admin.site.register(StudentFeedback)
admin.site.register(StudentLeave)
admin.site.register(Attendance)
admin.site.register(AttendenceReport)
admin.site.register(StudentResult)



