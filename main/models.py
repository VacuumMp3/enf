from django.db import models
from django.utils.text import slugify


class Category(models.Model):
    """ Категории товаров """

    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)


    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)


    def __str__(self):
        return self.name


class Size(models.Model):
    """ Размер товара ( M, L, XL, XXL, ... ) """

    name = models.CharField(max_length=32)


    def __str__(self):
        return self.name


class ProductSize(models.Model):
    """ Количество товаров """

    product = models.ForeignKey("Product", on_delete=models.CASCADE, related_name="product_sizes")
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    stock = models.PositiveIntegerField(default=0)


    def __str__(self):
         return f"{self.size.name} ({self.stock} in stock) for {self.product.name}"



class Product(models.Model):
    """ Товар """

    name = models.CharField(max_length=128)
    slug = models.CharField(max_length=128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    color = models.CharField(max_length=128)

    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True)
    main_image=models.ImageField(upload_to="products/main/")

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def save(self, *args, **kwargs):
            if not self.slug:
                self.slug = slugify(self.name)
            super().save(*args, **kwargs)

    
    def __str__(self):
        return self.name 


class ProductImage(models.Model):
    """ Изображение товаров """
    
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="products/extra")