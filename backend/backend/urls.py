"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from .views import *

urlpatterns = [
    path('api/login', Login.as_view(), name='login'),
    path('api/student/get_student_info', GetStudentInfo.as_view(), name='student'),
    path('api/student/get_student_grade', GetStudentGrade.as_view(), name='grade'),
    path('api/student/get_student_course', GetStudentCourse.as_view(), name='grade'),
    path('api/student/get_course_offering', GetCourseOffering.as_view(), name='grade'),
    path('api/teacher/get_teacher_info', GetTeacherInfo.as_view(), name='teacher'),
    path('api/teacher/get_teacher_course', GetTeacherCourse.as_view(), name='teacher'),
    path('api/teacher/teacher_get_student_grade', TeacherGetStudentGrade.as_view(), name='teacher'),
    path('api/teacher/update_student_grade', UpdateStudentGrade.as_view(), name='teacher'),
]
