from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.db.models import Avg, Count, Case, When, IntegerField
from .models import Employee, ContactMessage
from .serializers import ContactSerializer
from django.db.models import Avg
from django.http import JsonResponse
from .models import Employee
import json
from django.views.decorators.csrf import csrf_exempt

@api_view(['GET'])

def kpis(request):
   from django.http import JsonResponse
from django.db.models import Avg, Count
from .models import Employee


def kpis(request):
    qs = Employee.objects.all()

    # Optional filters from slicers
    department = request.GET.get("department")
    salary_band = request.GET.get("salaryBand")
    age_group = request.GET.get("ageGroup")

    if department and department != "All":
        qs = qs.filter(department=department)

    if salary_band and salary_band != "All":
        qs = qs.filter(salary_band=salary_band)

    if age_group and age_group != "All":
        qs = qs.filter(age_group=age_group)

    total_employees = qs.count()
    attrition_count = qs.filter(attrition="Yes").count()

    attrition_rate = (
        round((attrition_count / total_employees) * 100, 2)
        if total_employees > 0 else 0
    )

    avg_age = qs.aggregate(avg=Avg("age"))["avg"] or 0
    avg_salary = qs.aggregate(avg=Avg("monthly_income"))["avg"] or 0
    avg_years = qs.aggregate(avg=Avg("years_at_company"))["avg"] or 0

    data = {
        "total_employees": total_employees,
        "attrition_count": attrition_count,
        "attrition_rate": round(attrition_rate, 2),
        "avg_age": round(avg_age, 1),
        "avg_salary": round(avg_salary, 1),
        "avg_years": round(avg_years, 1),
    }

    return JsonResponse(data)



@api_view(['GET'])
def attrition_by_age(request):
    data = (
        Employee.objects
        .filter(attrition="Yes")
        .values("age_group")
        .annotate(count=Count("id"))
        .order_by("age_group")
    )
    return Response(data)

@api_view(['GET'])
def attrition_by_job_role(request):
    data = (
        Employee.objects
        .filter(attrition="Yes")
        .values("job_role")
        .annotate(count=Count("id"))
        .order_by("-count")
    )
    return Response(data)

@api_view(['GET'])
def attrition_by_salary_band(request):
    data = (
        Employee.objects
        .filter(attrition="Yes")
        .values("salary_band")
        .annotate(count=Count("id"))
        .order_by("salary_band")
    )
    return Response(data)


@api_view(['GET'])
def insights(request):
    insights = [
        "Higher attrition observed in low salary bands",
        "Early-career employees show higher turnover",
        "Sales and R&D departments experience higher attrition",
        "Compensation and experience are strong attrition drivers"
    ]

    return Response({
        "business_insights": insights
    })


@api_view(['POST'])
def contact(request):
    serializer = ContactSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"status": "success", "message": "Message sent"})
    return Response(serializer.errors, status=400)



def attrition_by_education(request):
    data = (
        Employee.objects
        .filter(attrition="Yes")
        .values("experience_group")   # ✅ existing field
        .annotate(count=Count("id"))
    )
    return JsonResponse(list(data), safe=False)



def attrition_by_years(request):
    data = (
        Employee.objects
        .filter(attrition="Yes")
        .values("years_at_company")
        .annotate(count=Count("id"))
        .order_by("years_at_company")
    )
    return JsonResponse(list(data), safe=False)


def attrition_by_gender(request):
    data = (
        Employee.objects
        .filter(attrition="Yes")
        .values("gender")
        .annotate(count=Count("id"))
    )
    return JsonResponse(list(data), safe=False)

@csrf_exempt
def contact(request):
    if request.method == "POST":
        data = json.loads(request.body)
        ContactMessage.objects.create(
            name=data["name"],
            email=data["email"],
            message=data["message"]
        )
        return JsonResponse({"status": "success"})
