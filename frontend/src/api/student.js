import axios from 'axios';
import {BASEURL} from "@/api/baseUrl.js";
export function getStudentInfo(){
    return axios.request({
        method: 'post',
        url: '/student/get_student_info',
        baseURL: BASEURL
    })
}

export function getStudentCourse(data){
    return axios.request({
        method: 'post',
        url: '/student/get_student_course',
        data,
        baseURL: BASEURL
    })
}

export function getStudentGrade(){
    return axios.request({
        method: 'post',
        url: '/student/get_student_grade',
        baseURL: BASEURL
    })
}

export function getCourseOffering(data){
    return axios.request({
        method: 'post',
        data:data,
        url: '/student/get_course_offering',
        baseURL: BASEURL
    })
}