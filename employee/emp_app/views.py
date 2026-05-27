import json
from http import HTTPStatus

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import EmployeeModel


@csrf_exempt
def add_employee(request):
    if request.method == "POST":
        try:
            if not request.body:
                return JsonResponse({"error": "Empty body"}, status=400)

            data = json.loads(request.body)

            emp = EmployeeModel.objects.create(
                emp_name=data.get("emp_name"),
                emp_email=data.get("emp_email"),
                emp_salary=data.get("emp_salary"),
                emp_phone=data.get("emp_phone"),
                emp_address=data.get("emp_address"),
                emp_join_date=data.get("emp_join_date"),
                emp_gender=data.get("emp_gender"),
                emp_age=data.get("emp_age"),
                emp_leave=data.get("emp_leave"),
            )

            return JsonResponse({
                "message": "Employee added successfully",
                "id": emp.id
            }, status=201)

        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)

        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only POST method allowed"}, status=405)


def get_employee_details(request):
    if request.method == "GET":
        try:
            employees = EmployeeModel.objects.all().values()
            return JsonResponse({
                "data": list(employees),
                "status": HTTPStatus.OK
            })
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Only GET method allowed"}, status=405)