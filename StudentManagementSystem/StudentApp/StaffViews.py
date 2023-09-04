from django.shortcuts import render , redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required



def StaffHome(request):
    # GetStaff = Staff.objects.get(admin = request.user.id)
    # GetSubjects = Subject.objects.filter(staff = GetStaff)
    # for i in GetSubjects:
        
    #     GetStudents = Student.objects.filter(course = i.course)
    #     print(GetStudents)
    
        
    # Context = {
    #     # 'Subject':Sub , 
    # }
    return render(request , 'Staff/Home.html' , )

def StaffNotificationView(request):
    StaffUser = Staff.objects.get(admin = request.user)
    Notification = StaffNotification.objects.filter(staff_id = StaffUser.id)
    Context = {
        'Notification':Notification,
    }
    return render(request , 'Staff/ViewNotification.html' , Context)

def StaffMarkAsDone(request , status):
    StaffNoti = StaffNotification.objects.get(id = status)
    StaffNoti.status = 1
    StaffNoti.save()
    return redirect('StaffNotificationView')


def StaffApplyLeave(request):
    Staffuser = Staff.objects.get(admin=request.user.id)
    StaffId = Staffuser.id
    StaffLeaveHistory = StaffLeave.objects.filter(staff_id=StaffId)
    Context = {
        'StaffLeaveHistory':StaffLeaveHistory,
    }
    return render(request, 'Staff/ApplyLeave.html' ,Context)


def StaffApplyLeaveSave(request):
    if request.method == "POST":
        LeaveDate = request.POST.get('LeaveDate')
        LeaveMessage = request.POST.get('LeaveMessage')
        StaffUser = Staff.objects.get( admin = request.user.id )
        
        StaffUserLeave = StaffLeave.objects.create(
            staff_id = StaffUser , 
            leavedate = LeaveDate , 
            message = LeaveMessage , 
        )
        StaffUserLeave.save()
        messages.success(request , 'Leave Apply Successfully')
        return redirect('StaffApplyLeave')
    
def StaffSendFeedBack(request):
    StaffUser = Staff.objects.get(admin = request.user.id )
    if request.method == "POST":
        Feedback = request.POST.get('Feedback')
        NewFeedback = StaffFeedback.objects.create(
            staff_id = StaffUser ,
            feedback = Feedback ,
        )
        NewFeedback.save()
        messages.success(request , 'FeedBack Sent Succefully')
        return redirect('StaffSendFeedBack')
    FeedbackHistory = StaffFeedback.objects.filter(staff_id = StaffUser)

    Context = {
        'FeedbackHistory':FeedbackHistory,  
    }
    return render(request , 'Staff/SendFeedback.html' ,Context)


def TakeAttendance(request):
    StaffUser = Staff.objects.get(admin = request.user.id)
    GetSubjects = Subject.objects.filter(staff = StaffUser)
    GetSession = Session.objects.all()
    
    GetSub = None
    GetSess = None
    Students = None
    action = request.GET.get('action')
    print(action , "Action")
    if action is not None:
        if request.method == 'POST':
            Subject_id = request.POST.get('Subject')
            Session_id = request.POST.get('Session')
            GetSub = Subject.objects.get(id = Subject_id)
            GetSess = Session.objects.get(id = Session_id)
            
            SubjectUsers = Subject.objects.filter(id = Subject_id)
            print(SubjectUsers , "SubjectUsers")
            for i in SubjectUsers:
                student_id = i.course.id
                Students = Student.objects.filter(course = student_id)
    Context = {
        'Subject':GetSubjects,
        'Session':GetSession,
        'GetSub':GetSub,
        'GetSess':GetSess,
        'action':action,
        'Students':Students,
    }       
    return render(request , 'Staff/TakeAttendance.html' , Context)


def Save_Attendance(request):
    if request.method == 'POST':
        GetSubject = request.POST.get('Subject')
        GetSession = request.POST.get('Session')
        GetAttenDanceDate = request.POST.get('AttenDanceDate')
        Students = request.POST.getlist('Students')

        GetSub = Subject.objects.get(id = GetSubject)
        GetSes = Session.objects.get(id = GetSession)     
        
        StudentAttendance = Attendance(
            subject_id = GetSub , 
            session_year_id = GetSes , 
            attendance_date = GetAttenDanceDate ,   
        ) 
        StudentAttendance.save()
        for i in Students:
            GetStudent = Student.objects.get(id= i)
            StudentAttendanceReport = AttendenceReport(
                student_id = GetStudent , 
                attendance_id = StudentAttendance , 
            )
            StudentAttendanceReport.save()
        return redirect('TakeAttendance')     
    
    
def View_Attendance(request):
    Users = Staff.objects.get(admin=request.user.id)
    GetSubjects = Subject.objects.filter(staff_id = Users)
    Sessions = Session.objects.all()
    action = request.GET.get('action')
    
    GetSub = None
    GetSess = None
    AttendanceDate = None
    Attendance_Report = None
    if action is not None:
        if request.method == "POST":
            Subject_id = request.POST.get('Subject')
            Session_id = request.POST.get('Session')
            AttendanceDate = request.POST.get('AttendanceDate')
            
            GetSub = Subject.objects.get(id = Subject_id)
            GetSess = Session.objects.get(id = Session_id)
            
            GetStudents = Attendance.objects.filter(subject_id = GetSub , attendance_date = AttendanceDate , session_year_id = GetSess )
            for i in GetStudents:
                StudentsId = i.id
                Attendance_Report = AttendenceReport.objects.filter(attendance_id = StudentsId ,)
           
    Context = {
        'Subject':GetSubjects,
        'Session':Sessions,
        'action':action,
        'GetSub':GetSub,
        'GetSess':GetSess,
        'AttendanceDate':AttendanceDate,
        'Attendance_Report':Attendance_Report,
    }
    
    
    return render(request , 'Staff/ViewAttendance.html' , Context)

def StaffAddResult(request):
    GetUser = Staff.objects.get(admin = request.user.id)
    GetSubjects = Subject.objects.filter(staff_id = GetUser)
    GetSession = Session.objects.all()
    action = request.GET.get('action')
    
    GetSub  = None
    GetSess = None
    Students = None
    if action is not None:
        if request.method == "POST":
            SubjectId = request.POST.get('Subject')
            SessionId = request.POST.get('Session')
            
            GetSub = Subject.objects.get(id = SubjectId)
            GetSess = Session.objects.get(id = SessionId)
            
            Subjects = Subject.objects.filter(id = SubjectId)
            for i in Subjects:
                StudentId = i.course.id
                Students = Student.objects.filter(course = StudentId)
               
           
    Context = {
        'Subject':GetSubjects,
        'Session':GetSession,
        'action':action,
        'GetSub':GetSub,
        'GetSess':GetSess,
        'Students':Students,
    }
    return render(request , 'Staff/AddResult.html' , Context)

def SaveResult(request):
    if request.method == "POST":
        SubjectId = request.POST.get('Subject')
        SessionId = request.POST.get('Session')
        StudentId = request.POST.get('student_id')
        assignment_mark = request.POST.get('assignment_mark')
        Exam_mark = request.POST.get('Exam_mark')
        if int(assignment_mark) >= 30 :
            messages.warning(request , 'assignmanet Marks should be less than 30') 
            return redirect('AddResult')
        if  int(Exam_mark) >= 70:
            messages.warning(request , 'Exam Marks should be less than 70') 
            return redirect('AddResult')
            
        GetStudent = Student.objects.get(admin = StudentId)
        GetSub = Subject.objects.get(id = SubjectId)
        
        StudentExist = StudentResult.objects.filter(subject_id = GetSub , student_id= GetStudent).exists()
        if StudentExist:
            result = StudentResult.objects.get(subject_id = GetSub , student_id= GetStudent )
            result.assignment_marks = assignment_mark
            result.exam_marks = Exam_mark
            result.save()
            messages.info(request , 'Result Are updated Successfully')
            return redirect('AddResult')
        else:
            result = StudentResult.objects.create(
                subject_id = GetSub ,
                student_id= GetStudent , 
                assignment_marks = assignment_mark ,
                exam_marks = Exam_mark   
            )
            result.save()
            messages.success(request , 'Result Successfully Added')
            return redirect('AddResult')