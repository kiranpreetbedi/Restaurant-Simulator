from django.db import models

class Category(models.Model):
   title = models.TextField()

class Chef(models.Model):
   title = models.TextField()

class Customer(models.Model):
   added_on = models.DateTimeField()
   updated_on = models.DateTimeField()
   order_items = models.TextField()
   delivery_time = models.DateTimeField()
   customer_title = models.TextField()

class Dish(models.Model):
   is_veg = models.IntegerField()
   dish_title = models.TextField()
   make_time = models.IntegerField()

class DishCategoryRelation(models.Model):
   dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
   category = models.ForeignKey(Category, on_delete=models.CASCADE)

class DishChefRelation(models.Model):
   chef = models.ForeignKey(Chef, on_delete=models.CASCADE)
   dish = models.ForeignKey(Dish, on_delete=models.CASCADE)
