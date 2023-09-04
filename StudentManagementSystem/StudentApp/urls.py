from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views , StaffViews , StudentViews , HodViews  

urlpatterns = [
    path('home' , views.base , name='base'),  
    path('Login' , views.LoginUser , name='LoginUser'), 
    path('' , views.DoLogin, name='DoLogin'),
    path('Do-Logout', views.DoLogOut, name='DoLogOut'),
    
    # Profile 
    path('Profile' , views.Profile , name='Profile'),
    path('Profile/Update' , views.ProfileUpdate , name='ProfileUpdate'),
        
    # HOd 
    path('HOD/Home' , HodViews.HodHome , name='HodHome'),
    
    path('HOD/Student_add' , HodViews.StudentAdd , name='StudentAdd'),
    path('HOD/Student_View' , HodViews.StudentView , name='StudentView'),
    path('HOD/Student-edit/<int:id>' , HodViews.StudentEdit , name='StudentEdit'),
    path('HOD/Student-Delete/<int:id>' , HodViews.StudentDelete , name='StudentDelete'),
    
    
    path('HOD/Course_add' , HodViews.CourseAdd , name='CourseAdd'),
    path('HOD/Course_View' , HodViews.CourseView , name='CourseView'),
    path('HOD/Course-edit/<int:id>' , HodViews.CourseEdit , name='CourseEdit'),
    path('HOD/Course-Delete/<int:id>' , HodViews.CourseDelete , name='CourseDelete'),
    
    
    path('HOD/Staff_add' , HodViews.StaffAdd , name='StaffAdd'),
    path('HOD/Staff_View' , HodViews.StaffView , name='StaffView'),
    path('HOD/Staff-edit/<int:id>' , HodViews.StaffEdit , name='StaffEdit'),
    path('HOD/Staff-Delete/<int:id>' , HodViews.StaffDelete , name='StaffDelete'),
    
    path('HOD/Subject_add' , HodViews.SubjectAdd , name='SubjectAdd'),
    path('HOD/Subject_View' , HodViews.SubjectView , name='SubjectView'),
    path('HOD/Subject-edit/<int:id>' , HodViews.SubjectEdit , name='SubjectEdit'),
    path('HOD/Subject-Delete/<int:id>' , HodViews.SubjectDelete , name='SubjectDelete'),
    
    
    path('HOD/Session_add' , HodViews.SessionAdd , name='SessionAdd'),
    path('HOD/Session_View' , HodViews.SessionView , name='SessionView'),
    path('HOD/Session-edit/<int:id>' , HodViews.SessionEdit , name='SessionEdit'),
    path('HOD/Session-Delete/<int:id>' , HodViews.SessionDelete , name='SessionDelete'),
    
    path('Hod/Staff/Leave/View' , HodViews.StaffLeaveView , name='StaffLeaveView'),
    path('Hod/Staff/leave_Approved/<int:id>' , HodViews.StaffLeaveApproved , name='StaffLeaveApproved'),
    path('Hod/Staff/leave_DisApproved/<int:id>' , HodViews.StaffLeaveDisApproved , name='StaffLeaveDisApproved'),
    path('Hod/Staff/Feedback' , HodViews.StaffFeedbackView , name='StaffFeedbackView'),
    path('Hod/Staff/Feedback/Save' , HodViews.StaffFeedbackSave , name='StaffFeedbackSave'),
    path('Hod/Student/Send_Notification' , HodViews.StudentSendNotifications , name='StudentSendNotifications'),
    path('Hod/Student/Feedback_View' , HodViews.StudentFeedbackView , name='StudentFeedbackView'),
    path('Hod/Student/Feedback/Save' , HodViews.StudentFeedbackSave , name='StudentFeedbackSave'),
    path('Hod/Student/Leave/View' , HodViews.StudentLeaveView , name='StudentLeaveView'),
    path('Hod/Student/leave_Approved/<int:id>' , HodViews.StudentLeaveApproved , name='StudentLeaveApproved'),
    path('Hod/Student/leave_DisApproved/<int:id>' , HodViews.StudentLeaveDisApproved , name='StudentLeaveDisApproved'),
    path('Hod/Student/View_Attendance' , HodViews.ViewAttendance , name='ViewAttendance'),
    
    
    
    
    
    
    # Staff Urls 
    path('Staff/Home' , StaffViews.StaffHome , name='StaffHome'),
    path('Hod/Staff/Notifications' , HodViews.Staff_Notifications , name='Staff_Notifications'),
    path('Hod/Save_Notifications' , HodViews.SaveStaffNotifications , name='SaveStaffNotifications') , 
    path('Staff/View/Notifications' , StaffViews.StaffNotificationView , name='StaffNotificationView'),
    path('Staff/MarkAsDone/<str:status>', StaffViews.StaffMarkAsDone ,name='StaffMarkAsDone' ),
    path('Staff/Apply_leave' , StaffViews.StaffApplyLeave, name='StaffApplyLeave'),
    path('Staff/Apply_leave/Save' , StaffViews.StaffApplyLeaveSave, name='StaffApplyLeaveSave'),
    path('Staff/Send_Feedback' , StaffViews.StaffSendFeedBack , name='StaffSendFeedBack'),
    path('Staff/Student/Take_Attendance' , StaffViews.TakeAttendance , name='TakeAttendance'),
    path('Staff/Save_Attendance' , StaffViews.Save_Attendance , name='Save_Attendance'),
    path('Staff/View_Attendance' , StaffViews.View_Attendance , name='View_Attendance'),
    path('Staff/Add_Result' , StaffViews.StaffAddResult , name='AddResult'),
    path('Staff/Save_Result' , StaffViews.SaveResult , name='SaveResult'),
    
    
    # Student Urls 
    path('Student/Home' , StudentViews.StudentHome , name='StudentHome'),
    path('Student/View_Notifications' , StudentViews.StudentViewNotification ,  name='StudentViewNotification'),
    path('Student/MarkAsDone/<str:status>', StudentViews.StudentMarkAsDone ,name='StudentMarkAsDone' ),
    path('Student/Send_Feedback' , StudentViews.StudentSendFeedBack , name='StudentSendFeedBack'),
    path('Student/Apply_leave' , StudentViews.StudentApplyLeave, name='StudentApplyLeave'),
    path('Student/Apply_leave/Save' , StudentViews.StudentApplyLeaveSave, name='StudentApplyLeaveSave'),
    path('Student/View_Attendance' , StudentViews.StudentViewAttendance , name='StudentViewAttendance'),
    path('Student/View_Result' , StudentViews.StudentViewResult , name='StudentViewResult'),
    
    
    
    
    
    
    
    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)