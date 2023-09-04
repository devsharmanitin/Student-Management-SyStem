from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

UserTypes = (
    ('Hod' , 'Hod'),
    ('Staff' , 'Staff'),
    ('Student' , 'Student'),
)


class CustomUser(AbstractUser):
    user_type = models.CharField(choices=UserTypes , max_length=20 , default='Student' , null=True)
    username = models.CharField(max_length=44,null=True,unique=True)
    profile = models.ImageField(upload_to='media/profile_pic' , null=True , default='static/assets/img/profiles/avatar-01.jpg')
    
    
    
class Course(models.Model):
    name = models.CharField(max_length=100 ,)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now_add=True , null=True)
    
    def __str__(self):
        return self.name
    
class Session(models.Model):
    SessionStart = models.DateField()
    SessionEnd = models.DateField()
    
    def __str__(self):
        return  f"{self.SessionStart} To {self.SessionEnd}"
    
    
             
        
    
  
class Student(models.Model):
    admin = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100 ,  )
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    session = models.ForeignKey(Session , on_delete=models.CASCADE)
    joining_at = models.DateField()
    Updated_at = models.DateField(auto_now_add=True)
    datebirth = models.DateField( null= True , blank= True)
    standard = models.PositiveIntegerField(null = True)
    mobilenumber = models.IntegerField(null= True)
    studentimage = models.ImageField(upload_to='media/profile_pic' , null=True)
    
    
    def __str__(self):
        return self.admin.first_name + " " + self.admin.last_name
    
    
    
class Staff(models.Model):
    admin = models.OneToOneField(CustomUser , on_delete=models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length=100)
    datebirth = models.DateField( null= True , blank= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.admin.username
    
    
class Subject(models.Model):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class StaffNotification(models.Model):
    staff_id = models.ForeignKey(Staff , on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True , default=0)
    
    def __str__(self):
        return self.staff_id.admin.first_name + '' + self.staff_id.admin.last_name
    
    
    
    
class StaffLeave(models.Model):
    staff_id = models.ForeignKey(Staff , on_delete=models.CASCADE)
    leavedate = models.DateField()
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + '' + self.staff_id.admin.last_name
        
        
        
class StaffFeedback(models.Model):
    staff_id = models.ForeignKey(Staff , on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)
    feedbackreply = models.CharField(max_length=1000 , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.staff_id.admin.first_name + '' + self.staff_id.admin.last_name
    
    
    
class StudentNotification(models.Model):
    student_id = models.ForeignKey(Student , on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(null=True , default=0)
    
    def __str__(self):
        return self.student_id.admin.first_name + '' + self.student_id.admin.last_name
    
class StudentFeedback(models.Model):
    student_id = models.ForeignKey(Student , on_delete=models.CASCADE)
    feedback = models.CharField(max_length=500)
    feedbackreply = models.CharField(max_length=1000 , null=True , blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + '' + self.student_id.admin.last_name
    
    
class StudentLeave(models.Model):
    student_id = models.ForeignKey(Student , on_delete=models.CASCADE)
    leavedate = models.DateField()
    message = models.TextField()
    status = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + '' + self.student_id.admin.last_name
    
    
class Attendance(models.Model):
    subject_id = models.ForeignKey(Subject , on_delete=models.CASCADE)
    attendance_date = models.DateField()
    session_year_id = models.ForeignKey(Session , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.subject_id.name
    
    
class AttendenceReport(models.Model):
    student_id = models.ForeignKey(Student , on_delete = models.CASCADE)
    attendance_id = models.ForeignKey(Attendance , on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + '' + self.student_id.admin.last_name
    
    
class StudentResult(models.Model):
    student_id = models.ForeignKey(Student , on_delete=models.CASCADE)
    subject_id = models.ForeignKey(Subject , on_delete=models.CASCADE)
    assignment_marks = models.PositiveIntegerField()
    exam_marks = models.PositiveIntegerField()
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    
    def __str__(self):
        return self.student_id.admin.first_name + '' + self.student_id.admin.last_name
    