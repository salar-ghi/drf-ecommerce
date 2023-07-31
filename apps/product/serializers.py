from rest_framework import serializers

from .models import Brand, Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    category = CategorySerializer()
    
    class Meta:
        model = Product
        fields = "__all__"

# from .class ModelName(models.Model):

#     def __str__(self):
#         pass

#     class Meta:
#         db_table = ''
#         managed = True
#         verbose_name = 'ModelName'
#         verbose_name_plural = 'ModelNames'