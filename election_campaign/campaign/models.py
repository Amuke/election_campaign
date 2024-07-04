from django.db import models

# Define a model for storing member information
class Member(models.Model):
    # Fields for member details
    name = models.CharField(max_length=100)  # Name of the member
    surname = models.CharField(max_length=100)  # Surname of the member
    email = models.EmailField(unique=True)  # Email address of the member, unique constraint
    cell_phone = models.CharField(max_length=15)  # Cell phone number of the member

    # String representation of the model instance
    def __str__(self):
        return f'{self.name} {self.surname}'
