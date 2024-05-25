from django.http import JsonResponse
from rest_framework.views import APIView

from .service import LoginService, StudentService, TeacherService
from uitls.response import Response
from uitls.tools import *


class Login(APIView):
    def post(self, request):
        account = request.data.get('username')
        password = request.data.get('password')
        response = LoginService.login(account, password)
        if response:
            return Response().ok(response, status=200)
        else:
            return Response().fail('登录失败', status=400)


class GetStudentInfo(APIView):
    def post(self, request):
        # 请求头获得token
        token = get_token_from_request(request)
        response = StudentService.get_student_info(token)
        if response:
            return Response().ok(response, status=200)
        else:
            return Response().fail('获取学生信息失败', status=400)


class GetStudentGrade(APIView):
    def post(self, request):
        # 请求头获得token
        token = get_token_from_request(request)
        response = StudentService.get_student_grade(token)
        if response:
            return Response().ok(response, status=200)
        else:
            return Response().fail('获取学生成绩失败', status=400)


class GetStudentCourse(APIView):
    def post(self, request):
        # 请求头获得token
        token = get_token_from_request(request)
        term = request.data.get('term')
        classId = request.data.get('classId')
        response = StudentService.get_student_course(token, term, classId)
        if response:
            return Response().ok(response, status=200)
        else:
            return Response().fail('获取学生课程失败', status=400)


class GetCourseOffering(APIView):
    def post(self, request):
        # 请求头获得token
        token = get_token_from_request(request)
        classId = request.data.get('classId')
        response = StudentService.get_course_offering(token, classId)
        if response:
            return Response().ok(response, status=200)
        else:
            return Response().fail('获取课程信息失败', status=400)


class GetTeacherInfo(APIView):
    def post(self, request):
        # 请求头获得token
        token = get_token_from_request(request)
        response = TeacherService.get_teacher_info(token)
        if response:
            return Response().ok(response, status=200)
        else:
            return Response().fail('获取教师信息失败', status=400)


class GetTeacherCourse(APIView):
    def post(self, request):
        # 请求头获得token
        token = get_token_from_request(request)
        response = TeacherService.get_teacher_course(token)
        if response:
            return Response().ok(response, status=200)
        else:
            return Response().fail('获取教师课程失败', status=400)


class TeacherGetStudentGrade(APIView):
    def post(self, request):
        # 请求头获得token
        token = get_token_from_request(request)
        classId = request.data.get('classId')
        courseId = request.data.get('courseId')
        response = TeacherService.teacher_get_student_grade(token, classId, courseId)
        if response:
            return Response().ok(response, status=200)
        else:
            return Response().fail('获取学生成绩失败', status=400)


class UpdateStudentGrade(APIView):
    def post(self, request):
        # 请求头获得token
        token = get_token_from_request(request)
        updateData = request.data.get('updateData')
        response = StudentService.update_student_grade(token, updateData)
        if response:
            return Response().ok(response, status=200)
        else:
            return Response().fail('升级学生成绩失败', status=400)