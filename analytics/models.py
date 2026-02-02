from django.db import models

class Employee(models.Model):
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    department = models.CharField(max_length=50)
    job_role = models.CharField(max_length=50)

    attrition = models.CharField(max_length=5)  # Yes / No

    monthly_income = models.FloatField()
    salary_band = models.CharField(max_length=20)

    total_working_years = models.IntegerField()
    years_at_company = models.IntegerField()
    experience_group = models.CharField(max_length=20)
    age_group = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.job_role} - {self.department}"


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
