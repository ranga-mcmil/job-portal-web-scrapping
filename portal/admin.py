from django.contrib import admin
from .models import JobPost, Category

# Register your models here.
@admin.register(JobPost)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'category','posted_by', 'link_to_job', 'expiry_date', 'posted_on',)

@admin.register(Category)
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
