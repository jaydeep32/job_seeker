from django.contrib import admin
from job.models import Category, Company, Job


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category_name",)}


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("job_name",)}


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass

