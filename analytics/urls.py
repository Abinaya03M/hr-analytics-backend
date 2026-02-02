# from django.urls import path
# from .views import *

# urlpatterns = [
#     path("kpis/", kpis),
#     path("attrition/age/", attrition_by_age),
#     path("attrition/job-role/", attrition_by_job_role),
#     path("attrition/salary-range/", attrition_by_salary_band),
#     # path("attrition/education/", attrition_by_education),
#     # path("attrition/years/", attrition_by_years),
#     # path("attrition/gender/",attrition_by_gender),

#     path("insights/", insights),
#     path("contact/", contact),
# ]
from django.urls import path
from . import views

urlpatterns = [
    path("kpis/", views.kpis),

    path("attrition/age/", views.attrition_by_age),
    path("attrition/job-role/", views.attrition_by_job_role),
path("attrition/salary-range/", views.attrition_by_salary_band),
    

    path("attrition/education/", views.attrition_by_education),
    path("attrition/years/", views.attrition_by_years),
    path("attrition/gender/", views.attrition_by_gender),
    path("contact/", views.contact),
    
]
