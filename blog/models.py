from django.db import models
# from blog.models import CategoryModel


class CategoryModel(models.Model):
    class Meta:
        db_table = "category"

    category_name = models.CharField(max_length=124)
    description = models.CharField(max_length=124)


    
class ArticleModel(models.Model):
    class Meta:
        db_table = "article"

    title = models.CharField(max_length=124)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=1024)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


