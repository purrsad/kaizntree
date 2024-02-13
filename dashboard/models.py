from django.db import models
from django.contrib.auth.models import User


class UserDetails(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
        ('N', 'Non-binary'),
    )
    USER_TYPE_CHOICES = (
        ('u1', 'user1'),
        ('u2', 'user2'),
    )
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, auto_now=True)

    userId = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False)
    firstName = models.CharField(max_length=100, null=True, blank=True)
    lastName = models.CharField(max_length=100, null=True, blank=True)
    gender = models.CharField(null=True, blank=True, choices=GENDER_CHOICES, max_length=1)
    userType = models.CharField(choices=USER_TYPE_CHOICES, null=True, blank=True, max_length=2)
    email_address = models.EmailField(null=True, blank=True, max_length=100)
    phone_number = models.CharField(null=True, blank=True, max_length=15)

    isInActive = models.BooleanField(default=False)
    isInActiveDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}, Type: {self.userType}"


class Category(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, auto_now=True)

    category_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")

    isInActive = models.BooleanField(default=False)
    isInActiveDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.category_name


class Items(models.Model):
    dateCreated = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    dateModified = models.DateTimeField(null=True, blank=True, auto_now=True)

    sku_code = models.CharField(max_length=50, null=True, blank=True)
    item_name = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(null=True, blank=True, default="Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.")
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, null=False, blank=False)
    tags = models.JSONField(null=True, blank=True)
    in_stock = models.IntegerField(null=True, blank=True)
    available_stock = models.IntegerField(null=True, blank=True)
    units = models.CharField(max_length=100, null=True, blank=True)
    minimum_stock = models.IntegerField(null=True, blank=True)
    desired_stock = models.IntegerField(null=True, blank=True)
    cost = models.FloatField(null=True, blank=True)
    assembly_flag = models.BooleanField(default=False)
    purchaseable_flag = models.BooleanField(default=False)
    component_flag = models.BooleanField(default=False)
    salable_flag = models.BooleanField(default=False)
    bundle_flag = models.BooleanField(default=False)

    isInActive = models.BooleanField(default=False)
    isInActiveDate = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.sku_code} {self.item_name}, Cost: {self.cost}"
