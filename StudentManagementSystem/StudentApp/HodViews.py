from django.shortcuts import render , redirect
from django.contrib.auth.decorators import login_required
from .models import *
from django.contrib import messages
from django.http import HttpResponse

@login_required(login_url= '/')
def HodHome(request):
    GetStudent = Student.objects.all()
    GetStaff = Staff.objects.all()
    GetCourse = Course.objects.all()
    GetSubject = Subject.objects.all()
    
    GetStudentCount = GetStudent.count() 
    GetStaffCount = GetStaff.count() 
    GetCourseCount = GetCourse.count() 
    GetSubjectCount = GetSubject.count() 
    
    StudentGenderMale = Student.objects.filter(gender = "Male")
    StudentGenderFemale = Student.objects.filter(gender = "Female")

    
    StudentGenderMaleCount = StudentGenderMale.count()
    StudentGenderFemaleCount = StudentGenderFemale.count()
    # years = Student.objects.values_list('joining_at' , flat=True)
   
    
    Context = {
        
        'GetStudentCount':GetStudentCount , 
        'GetStaffCount':GetStaffCount ,
        'GetCourseCount':GetCourseCount ,
        'GetSubjectCount':GetSubjectCount,
        'StudentGenderMaleCount':StudentGenderMaleCount ,
        'StudentGenderFemaleCount':StudentGenderFemaleCount, 
         
    }
    
    return render(request , 'Hod/Home.html' ,Context)

@login_required(login_url= '/')
def StudentAdd(request):
    course = Course.objects.all()
    session = Session.objects.all()
    if request.method == "POST":
        StudentImage = request.FILES.get("StudentImage")
        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        StudentEmail = request.POST.get("StudentEmail")
        Username = request.POST.get("Username")
        Dob = request.POST.get("Dob")
        Gender = request.POST.get("Gender")
        Standard = request.POST.get("Standard")
        JoiningData = request.POST.get("JoiningData")
        number = request.POST.get("Number")
        CourseId = request.POST.get("Course")
        SessionId = request.POST.get("Session")
        Address = request.POST.get("Address")
        Password = request.POST.get("Password")
        Number = int(number)
        
        if CustomUser.objects.filter(email = StudentEmail).exists():
            messages.warning(request , 'Email Already Exists')
            return redirect('StudentAdd')
        if CustomUser.objects.filter(username = Username).exists():
            messages.warning(request , 'Username Already Exists')
            return redirect('StudentAdd')
        else:
            NewUser = CustomUser.objects.create(
                first_name = FirstName ,
                last_name = LastName , 
                email = StudentEmail ,
                username = Username , 
                profile = StudentImage , 
                user_type = "Student" ,                  
                )         
            NewUser.set_password(Password)
            
            StudentCourse = Course.objects.get(id = CourseId)
            StudentSession = Session.objects.get(id = SessionId)
            NewStudent = Student.objects.create(
                admin = NewUser , 
                address = Address , 
                session = StudentSession , 
                course = StudentCourse , 
                gender = Gender , 
                standard = Standard , 
                datebirth = Dob ,
                joining_at =  JoiningData , 
                mobilenumber = Number ,   
            ) 
            NewUser.save()
            NewStudent.save()
            messages.success(request , f"{FirstName} Is Created")
            return redirect('StudentAdd')
       
    Context = {
        'Session':session , 
        'Course':course,
    }
    return render(request , 'Hod/AddStudent.html' , Context)


@login_required(login_url= '/')
def StudentView(request):
    Students = Student.objects.all()
    Context = {
        'Student':Students,
    }
    return render(request, 'Hod/ViewStudent.html' , Context)

@login_required(login_url= '/')
def StudentEdit(request , id):
    if request.method == "GET":
        StudentData = Student.objects.get(id = id)
        Courses = Course.objects.all()
        Sessions = Session.objects.all()
        Context = {
            'Student':StudentData , 
            'Courses': Courses , 
            'Sessions': Sessions,
        }
        return render(request , 'Hod/EditStudent.html' , Context)
    else:
        StudentImage = request.FILES.get("StudentImage")
        FirstName = request.POST.get("FirstName")
        LastName = request.POST.get("LastName")
        StudentEmail = request.POST.get("StudentEmail")
        Username = request.POST.get("Username")
        Dob = request.POST.get("Dob")
        Gender = request.POST.get("Gender")
        Standard = request.POST.get("Standard")
        JoiningData = request.POST.get("JoiningData")
        number = request.POST.get("Number")
        CourseId = request.POST.get("Course")
        SessionId = request.POST.get("Session")
        Address = request.POST.get("Address")
        Password = request.POST.get("Password")
        
        NewStudent = Student.objects.get(id = id) 
        NewUser = CustomUser.objects.get(username = NewStudent.admin.username)
        
        NewUser.first_name = FirstName 
        NewUser.last_name = LastName 
        NewUser.email = StudentEmail 
        NewUser.username = Username 
        if Password != None and Password != "":
            NewUser.set_password(Password)
        if StudentImage != None and StudentImage != "":
            NewUser.profile = StudentImage
            
        NewStudent.datebirth = Dob
        NewStudent.gender = Gender
        NewStudent.standard = Standard
        NewStudent.joining_at = JoiningData
        NewStudent.mobilenumber = number
        NewStudent.course.id = CourseId
        NewStudent.session.id = SessionId
        NewStudent.address = Address
        NewStudent.save()
        NewUser.save()
        messages.info(request , f'{FirstName }Data Updated Successfully')
        return redirect('StudentView' )
    
    
    
    
@login_required(login_url= '/')
def StudentDelete(request , id):
    NewStudent = Student.objects.get(id=id) 
    User = CustomUser.objects.get(username = NewStudent.admin.username)
    NewStudent.delete()
    User.delete()
    messages.info(request , 'f{User} Deleted Successfully')
    return redirect('StudentView')


@login_required(login_url= '/')
def CourseAdd(request):
    if request.method == "POST":
        course = request.POST.get('Course')
        courseAdd = Course.objects.create( name = course )
        courseAdd.save()
        messages.info(request , 'COurse Added Successfully')
        return redirect('CourseAdd')
    return render(request , 'Hod/AddCourse.html')


@login_required(login_url= '/')
def CourseView(request):
    Courses = Course.objects.all()
    Context = {
        'Courses':Courses,
    }
    return render(request , 'Hod/ViewCourse.html' , Context)

@login_required(login_url= '/')
def CourseEdit(request , id):
    if request.method == "GET":
        Courses = Course.objects.get(id=id)
        Context = {
            'Courses':Courses,
        }
        return render(request , 'Hod/EditCourse.html' , Context)
        
    else:
        GetCourse = request.POST.get('Course')
        course = Course.objects.get(id=id)
        course.name = GetCourse
        course.save()
        messages.info(request , 'Course Updated Successfully')
        return redirect('CourseView')
    
@login_required(login_url= '/')
def CourseDelete(request , id):
    print(id)
    course = Course.objects.get(id=id)
    print(course)
    course.delete()
    messages.info(request , 'COurse Deleted Successfully')
    return redirect('CourseView')

@login_required(login_url= '/')
def StaffAdd(request):
    if request.method == "POST":
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        StaffEmail = request.POST.get('StaffEmail')
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        Dob = request.POST.get('Dob')
        Gender = request.POST.get('Gender')
        StaffImage = request.FILES.get('StaffImage')
        Address = request.POST.get('Address')
        if CustomUser.objects.filter(email = StaffEmail).exists():
            messages.warning(request , 'Email Already Exists')
            return redirect('StaffAdd')
        if CustomUser.objects.filter(username = Username).exists():
            messages.warning(request , 'Username Already Exists')
            return redirect('StaffAdd')
        else:
            NewUser = CustomUser.objects.create(
                first_name = FirstName ,
                last_name = LastName , 
                email = StaffEmail ,
                username = Username , 
                profile = StaffImage , 
                user_type = "Staff" ,                  
                )         
            NewUser.set_password(Password)
            
            NewStaff = Staff.objects.create(
                admin = NewUser , 
                address = Address , 
                gender = Gender ,  
                datebirth = Dob ,  
            ) 
            NewUser.save()
            NewStaff.save()
            messages.success(request , f"{FirstName} Staff User Is Created")
            return redirect('StaffAdd')    
    return render(request , 'Hod/AddStaff.html')

@login_required(login_url= '/')
def StaffView(request):
    staff = Staff.objects.all()
    Context = {
        'Staff':staff,
    }
    return render(request , 'Hod/ViewStaff.html' , Context)

@login_required(login_url= '/')
def StaffEdit(request , id):
    if request.method == "GET":
        StaffUser = Staff.objects.get(id=id)
        Context = {
            'StaffUser':StaffUser , 
        }
        return render(request , 'Hod/EditStaff.html'  , Context)
    else:
        FirstName = request.POST.get('FirstName')
        LastName = request.POST.get('LastName')
        StaffEmail = request.POST.get('StaffEmail')
        Username = request.POST.get('Username')
        Password = request.POST.get('Password')
        Dob = request.POST.get('Dob')
        Gender = request.POST.get('Gender')
        StaffImage = request.FILES.get('StaffImage')
        Address = request.POST.get('Address')
        
        StaffUser = Staff.objects.get( id = id )
        User = CustomUser.objects.get(username = StaffUser.admin.username)
        
        User.last_name = LastName 
        User.first_name = FirstName 
        User.email = StaffEmail 
        User.username = Username 
        if Password != None and Password != "":
            User.set_password(Password)
        if StaffImage != None and StaffImage != "":
            User.profile = StaffImage
            
        StaffUser.datebirth = Dob
        StaffUser.gender = Gender
        StaffUser.address = Address
        
        User.save()
        StaffUser.save()
        messages.success(request , f"{FirstName} Staff User Is Updated Successfully")
        return redirect('StaffView') 
    
    
@login_required(login_url= '/')
def StaffDelete(request , id):
    StaffUser = Staff.objects.get(id=id)
    StaffUser.delete()
    return redirect('StaffView')
    
    
@login_required(login_url= '/')
def SubjectAdd(request):
    if request.method == "GET":
        course = Course.objects.all()
        staffUser = Staff.objects.all()
        print(course)
        print(staffUser)
        Context = {
            'Course':course ,
            'Staff':staffUser, 
        }
        return render(request , 'Hod/AddSubject.html' , Context)
    else:
        course = request.POST.get('Course')
        SubjectName = request.POST.get('SubjectName')
        staff = request.POST.get('Staff')
        
        NewCourse = Course.objects.get(id = course)
        StaffUser = Staff.objects.get(id = staff)
        
        NewSubject = Subject.objects.create(
            name = SubjectName , course = NewCourse , staff = StaffUser
        )
        NewSubject.save()
        messages.success(request , 'Subject Is added')
        return redirect('SubjectAdd')
        
@login_required(login_url= '/')
def SubjectView(request):
    subject = Subject.objects.all()
    Context = {
        'Subject':subject , 
    }
    return render(request , 'Hod/ViewSubject.html' ,Context)


@login_required(login_url= '/')
def SubjectEdit(request , id):
    if request.method == "GET":
        SubJectUser = Subject.objects.get(id = id)
        course = Course.objects.all()
        staff = Staff.objects.all()
        Context = {
            'Subject':SubJectUser,
            'Course':course,
            'Staff':staff,
        }
        return render(request , 'Hod/EditSubject.html' , Context)
    else:
        NewSubject = request.POST.get('SubjectId')
        NewSubjectName = request.POST.get('SubjectName')
        NewCourse = request.POST.get('Course')
        NewStaff = request.POST.get('Staff')
        
        Newcourse = Course.objects.get(id = NewCourse)
        Newstaff = Staff.objects.get(id = NewStaff)
        subject = Subject.objects.get(id = NewSubject)  
        
        subject.name =  NewSubjectName,
        subject.course.id = Newcourse , 
        subject.staff.id = Newstaff,
        
        subject.save()
        messages.success(request , 'Subject Updated Succssfully')
        return redirect('SubjectView')



@login_required(login_url= '/')
def SubjectDelete(request , id):
    NewSubject = Subject.objects.get(id=id)
    NewSubject.delete()
    return redirect('SubjectView')
    
    
    
@login_required(login_url= '/')
def SessionAdd(request):
    if request.method == "POST":
        StartSession = request.POST.get('SessionStart')
        EndSession = request.POST.get('SessionEnd')
        NewSession = Session.objects.create(
            SessionStart = StartSession , 
            SessionEnd = EndSession ,
        )
        NewSession.save()
        messages.success(request , 'Session is Created')
        return redirect('SessionAdd') 
    return render(request , 'Hod/AddSession.html')

@login_required(login_url= '/')
def SessionView(request):
    GetSession = Session.objects.all()
    Context = {
        'Session' : GetSession ,
    }
    return render(request , 'Hod/ViewSession.html' ,Context)

@login_required(login_url= '/')
def SessionEdit(request , id):
    if request.method == "GET":
        GetSession = Session.objects.get(id=id)
        Context = {
            'Session':GetSession ,
        }
        return render(request , 'Hod/EditSession.html' , Context)
    else:
        StartSession = request.POST.get('SessionStart')
        EndSession = request.POST.get('SessionEnd')
        
        GetSession = Session.objects.get(id=id)
        GetSession.SessionStart = StartSession
        GetSession.SessionEnd = EndSession
        GetSession.save()
        messages.success(request , 'Session updated Successfully')
        return redirect('SessionView')

@login_required(login_url= '/')
def SessionDelete(request , id):
    GetSession = Session.objects.get(id=id)
    GetSession.delete()
    messages.warning(request , 'Session Deleted Sucessfully')
    return redirect('SessionView')
    
    
@login_required(login_url= '/')
def Staff_Notifications(request):
    staff = Staff.objects.all()
    StatusNoti = StaffNotification.objects.all().order_by('-id')[0:5]
    Context = {
        'Staff':staff , 
        'StatusNoti':StatusNoti,
    }
    return render(request , 'Hod\StaffNotifications.html' , Context)

@login_required(login_url= '/')
def SaveStaffNotifications(request):
    if request.method == "POST":
        Staff_id = request.POST.get('Staff_id')
        Message = request.POST.get('SendNotification')

        StaffUser = Staff.objects.get(id = Staff_id)
        NewNotification = StaffNotification.objects.create(
            staff_id = StaffUser , 
            message = Message ,   
        )
        NewNotification.save()
        messages.success(request , 'Notification Send Successfully')
        return redirect('Staff_Notifications')
    
@login_required(login_url= '/')  
def StaffLeaveView(request):
    ApplyLeaveStaff = StaffLeave.objects.all()
    Context = {
        'Applyleave':ApplyLeaveStaff ,
    }
    return render(request , 'Hod/ViewStaffLeave.html' , Context)

@login_required(login_url= '/')
def StaffLeaveApproved(request , id ):
    StaffUser = StaffLeave.objects.get( id = id )
    StaffUser.status = 1
    StaffUser.save()
    return redirect('StaffLeaveView')

@login_required(login_url= '/')
def StaffLeaveDisApproved(request , id):
    StaffUser = StaffLeave.objects.get( id = id )
    StaffUser.status = 2
    StaffUser.save()
    return redirect('StaffLeaveView')

def StaffFeedbackView(request):
    StaffUsers = StaffFeedback.objects.all()
    StaffUser = Staff.objects.all() 
    Context = {
        'StaffUser':StaffUsers,
        'Staff':StaffUser,
    }
    return render(request , 'Hod/StaffFeedbackReply.html', Context)


    
def StaffFeedbackSave(request):
    if request.method == "POST":
        StaffFeedbackReply = request.POST.get('ReplyFeedback')
        StaffId = request.POST.get('Staff_id')
        StaffFeedUser = StaffFeedback.objects.get(id = StaffId)
        StaffFeedUser.feedbackreply = StaffFeedbackReply
        StaffFeedUser.save()
        return redirect('StaffFeedbackView')
   
   
def StudentSendNotifications(request):
    StudentUsers = Student.objects.all()
    NewNoti = StudentNotification.objects.all()
    Context = {
        'Student':StudentUsers,
        'NewNoti':NewNoti,
    }
    if request.method == "POST":
        Staff_id = request.POST.get('Staff_id')
        StudentSendNotification = request.POST.get('SendNotification')
        StudentUser = Student.objects.get(id=Staff_id)
        
        NewNotification = StudentNotification.objects.create(
            student_id = StudentUser ,
            message = StudentSendNotification,
            )
        NewNotification.save()
        return redirect('StudentSendNotifications')
    return render(request , 'Student/StudentSendNotifications.html' , Context)


def StudentFeedbackView(request):
    StudentUser = StudentFeedback.objects.all()
    Students = Student.objects.all()
    Context = {
        'StudentUser':StudentUser,
    }
    return render(request , 'Hod/StudentFeedbackView.html' , Context)

def StudentFeedbackSave(request):
    if request.method == "POST":
        StaffFeedbackReply = request.POST.get('ReplyFeedback')
        StaffId = request.POST.get('Staff_id')
        StaffFeedUser = StudentFeedback.objects.get(id = StaffId)
        StaffFeedUser.feedbackreply = StaffFeedbackReply
        StaffFeedUser.save()
        return redirect('StudentFeedbackView')
    
    
@login_required(login_url= '/')  
def StudentLeaveView(request):
    ApplyLeaveStaff = StudentLeave.objects.all()
    Context = {
        'Applyleave':ApplyLeaveStaff ,
    }
    return render(request , 'Hod/ViewStudentLeave.html' , Context)

@login_required(login_url= '/')
def StudentLeaveApproved(request , id ):
    StaffUser = StudentLeave.objects.get( id = id )
    StaffUser.status = 1
    StaffUser.save()
    return redirect('StudentLeaveView')

@login_required(login_url= '/')
def StudentLeaveDisApproved(request , id):
    StaffUser = StudentLeave.objects.get( id = id )
    StaffUser.status = 2
    StaffUser.save()
    return redirect('StaffLeaveView')

def ViewAttendance(request):
    GetSubjects = Subject.objects.all()
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
    return render(request , 'Hod/ViewAttendance.html' , Context )