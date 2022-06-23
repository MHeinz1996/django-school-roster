from django.shortcuts import render
from .models import School # import our School class

my_school = School("Django School") # create a school instance


def index(request):
    my_data = { 
        "school_name": my_school.name
    }
    return render(request, "app/index.html", my_data)


def list_staff(request):
    data = {'all_staff': my_school.staff}
    return render(request, "app/list_staff.html", data)


def staff_detail(request, employee_id):
    staff = my_school.find_staff_by_id(employee_id)
    data = {"staff": staff}
    return render(request, "app/staff_detail.html", data)


def list_students(request):
    data = {'all_students': my_school.students}
    return render(request, "app/list_students.html", data)


def student_detail(request, school_id):
    student = my_school.find_student_by_id(school_id)
    data = {"student": student}
    return render(request, "app/student_detail.html", data)