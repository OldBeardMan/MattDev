from django.db import models
from django.core.validators import RegexValidator

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    image = models.ImageField(upload_to='testimonials/')
    content = models.TextField()

    def __str__(self):
        return f"{self.name} from {self.company}"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(
        max_length=9,
        blank=True,
        null=True,
        validators=[RegexValidator(r'^\d{9}$', 'Phone number must be exactly 9 digits')]
    )
    company = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()

    def __str__(self):
        return self.name
