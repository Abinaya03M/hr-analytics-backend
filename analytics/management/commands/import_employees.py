import csv
from django.core.management.base import BaseCommand
from django.conf import settings
from analytics.models import Employee
import os

class Command(BaseCommand):
    help = "Import employees from CSV"

    def handle(self, *args, **kwargs):
        file_path = os.path.join(settings.BASE_DIR, "employee_attrition_cleaned.csv")

        self.stdout.write(self.style.WARNING(f"Reading file: {file_path}"))

        with open(file_path, newline="", encoding="utf-8-sig") as csvfile:
            reader = csv.DictReader(csvfile)

            self.stdout.write(self.style.WARNING(f"CSV Columns: {reader.fieldnames}"))

            rows = list(reader)
            self.stdout.write(self.style.WARNING(f"Total rows found in CSV: {len(rows)}"))

            count = 0
            for row in rows:
                Employee.objects.create(
                    age = int(row["Age"]),
                    gender = row["Gender"],
                    department = row["Department"],
                    job_role = row["Job Role"],
                    attrition = row["Attrition"],
                    monthly_income = float(row["Monthly Income"]),
                    salary_band = row["Salary_Band"],
                    total_working_years = int(row["TotalWorkingYears"]),
                    years_at_company = int(row["Years At Company"]),
                    experience_group = row["Experience_Group"],
                    age_group = row["Age_Group"],
                )
                count += 1

            self.stdout.write(self.style.SUCCESS(f"Imported {count} employees successfully"))
