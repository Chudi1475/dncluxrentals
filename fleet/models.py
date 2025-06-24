from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

class Vehicle(models.Model):
    category    = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='vehicles')
    name        = models.CharField(max_length=100)
    slug        = models.SlugField(unique=True)
    description = models.TextField()
    image       = models.ImageField(upload_to='vehicles/')
    rate        = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name

class Testimonial(models.Model):
    author = models.CharField(max_length=100)
    text   = models.TextField()
    stars  = models.PositiveSmallIntegerField(default=5)

    def __str__(self):
        return f"{self.author} ({self.stars}★)"

class ContactMessage(models.Model):
    first_name = models.CharField(max_length=50)
    last_name  = models.CharField(max_length=50)
    email      = models.EmailField()
    message    = models.TextField()
    created    = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Booking(models.Model):
    vehicle             = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    name                = models.CharField(max_length=100)
    phone               = models.CharField(max_length=20)
    email               = models.EmailField()
    start_date          = models.DateField()
    end_date            = models.DateField()
    need_insurance      = models.BooleanField(default=False)
    extension_requested = models.BooleanField(default=False)
    created             = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Booking: {self.vehicle.name} by {self.name}"
