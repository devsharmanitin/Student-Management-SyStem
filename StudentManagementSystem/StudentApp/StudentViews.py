from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.contrib import messages

def StudentHome(request):
    return render(request , 'Student/Home.html')

def StudentViewNotification(request):
    StudentUser = Student.objects.get(admin = request.user.id )
    
    StudentNoti = StudentNotification.objects.filter(student_id = StudentUser)
    Context = {
        'Notification':StudentNoti,
    }
    return render(request , 'Student/StudentViewNotifications.html' , Context)

def StudentMarkAsDone(request , status):
    StudentUser = StudentNotification.objects.get(id = status)
    StudentUser.status = 1
    StudentUser.save()
    return redirect('StudentViewNotification')

def StudentSendFeedBack(request):
    StudentUser = Student.objects.get(admin = request.user.id)
    if request.method == "POST":
        Feedback = request.POST.get('Feedback')
        NewFeedback = StudentFeedback.objects.create(
            student_id = StudentUser , 
            feedback = Feedback , 
        )
        NewFeedback.save()
        return redirect('StudentSendFeedBack')
    GetFeedback = StudentFeedback.objects.filter(student_id = StudentUser)
    print(GetFeedback )
    Context = {
        'FeedbackHistory':GetFeedback,
    }
    return render(request , 'Student/SendFeedback.html' , Context)


def StudentApplyLeave(request):
    Staffuser = Student.objects.get(admin=request.user.id)
    StaffId = Staffuser.id
    StaffLeaveHistory = StudentLeave.objects.filter(student_id=StaffId)
    Context = {
        'StaffLeaveHistory':StaffLeaveHistory,
    }
    return render(request, 'Student/ApplyLeave.html' ,Context)

def StudentApplyLeaveSave(request):
    if request.method == "POST":
        LeaveDate = request.POST.get('LeaveDate')
        LeaveMessage = request.POST.get('LeaveMessage')
        StaffUser = Student.objects.get( admin = request.user.id )
        
        StaffUserLeave = StudentLeave.objects.create(
            student_id = StaffUser , 
            leavedate = LeaveDate , 
            message = LeaveMessage , 
        )
        StaffUserLeave.save()
        messages.success(request , 'Leave Apply Successfully')
        return redirect('StudentApplyLeave')
    
    
def StudentViewAttendance(request):
    Users = Student.objects.get(admin=request.user.id)
    GetSubjects = Subject.objects.filter(course = Users.course)
    action = request.GET.get('action')

    
    GetSub =  None
    GetAttendanceReport = None
    if action is not None:
        if request.method == "POST":
            Subject_id = request.POST.get('Subject')
            GetSub = Subject.objects.get(id = Subject_id)
            GetAttendanceReport = AttendenceReport.objects.filter( student_id = Users , attendance_id__subject_id = Subject_id)
    
    Context = {
        'GetSubjects':GetSubjects,
        'action':action,
        'GetSub':GetSub,
        'GetAttendanceReport':GetAttendanceReport,
    }
    return render(request , 'Student/ViewAttendance.html' , Context)

def StudentViewResult(request):
    GetStudent = Student.objects.get(admin = request.user.id)
    GetStudentResult = StudentResult.objects.filter(student_id = GetStudent)
    for i in GetStudentResult:
        assignMarks = i.assignment_marks 
        exam_mark = i.exam_marks
        mark = int(assignMarks) + int(exam_mark)
    Context = {
        'Result':GetStudentResult,
        'mark':mark,
    }
    return render(request , 'Student/ViewResult.html' , Context)