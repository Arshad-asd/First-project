from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models
from django.utils.translation import gettext_lazy as _
from phonenumber_field.modelfields import PhoneNumberField
# Create your models here.

class CustomUserManager(BaseUserManager):
    """Define a model manager for User model with no username field."""

    def _create_user(self, email, password=None, **extra_fields):
        """Create and save a User with the given email and password."""
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password=None, **extra_fields):
        """Create and save a SuperUser with the given email and password."""
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(email, password, **extra_fields)



class CustomUser(AbstractUser):
    username = None
    email = models.EmailField(_('email address'), unique=True)
    name = models.CharField(_('name'), max_length=30, blank=True)
    mobile = PhoneNumberField(_('mobile number'), blank=True, null=True)
    otp = models.CharField(_('OTP'), max_length=6, blank=True)


    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
       return self.email
class Product(models.Model):
    Product_name = models.CharField(max_length=255)
    description = models.TextField()
    Product_Image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey('Category', on_delete=models.CASCADE)


    def __str__(self):
        return self.name

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=8, decimal_places=2,default=0)
    Quantity = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.size} - {self.product.name}"

class Category(models.Model):
    categoryes = models.CharField(max_length=50)

    def __str__(self):
        return self.categoryes