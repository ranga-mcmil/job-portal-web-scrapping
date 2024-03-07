from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, db_index=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def get_absolute_url(self):
        return reverse('portal:job_list_by_category', args=[self.slug])

    def __str__(self):
        return f'{self.name}'

# Create your models here.
class JobPost(models.Model):
    title = models.CharField(max_length=100) 
    posted_by = models.CharField(max_length=100, null=True, blank=True) 
    link_to_job = models.URLField(max_length=200) 
    expiry_date = models.CharField(max_length=30, null=True, blank=True) 
    posted_on = models.CharField(max_length=30, null=True, blank=True) 
    description = models.TextField()  
    category = models.ForeignKey(Category, related_name='posts', on_delete=models.CASCADE, null=True, blank=True) 
