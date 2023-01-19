from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=155)

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categoies'

    def __str__(self):
        return f"{self.title}"


class Product(models.Model):
    image = models.ImageField(upload_to='product/')
    title = models.CharField(max_length=155)
    text = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey('app.Category', models.CASCADE)

    def __str__(self):
        return f'{self.title} ${self.price}'

    # class Meta:
    #     # managed = False
    #     db_table = 'product'
