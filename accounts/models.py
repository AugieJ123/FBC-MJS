from django.db import models
from django.urls import reverse_lazy

class RegistrationForm(models.Model):
    Gender = (
        ('Male', 'Male'),
        ('Female', 'Female'),
    )

    Marital_Status = (
        ('Single', 'Single'),
        ('Married', 'Married'),
        ('Divorce', 'Divorce')
    )

    IslamicKnowledge = (
        ('None', 'None'),
        ('Basic', 'Basic'),
        ('Intermediate', 'Intermediate')
    )

    serve_in_organization = (
        ('No', 'No'),
        ('Yes', 'Yes')
    )



    registration_number = models.IntegerField(blank=False, null=False)

    surname = models.CharField(max_length=50, blank=False, null=False)
    other_name = models.CharField(max_length=60, blank=False, null=False)
    course = models.CharField(max_length=60, blank=False, null=False)
    gender = models.CharField(choices=Gender, max_length=19, blank=False, null=False, default='Male')

    date_of_birth = models.DateField(blank=True, null=True)
    place_of_birth = models.CharField(max_length=100, blank=True, null=True)
    contact_address = models.CharField(max_length=150, blank=False, null=False)
    contact_number = models.CharField(max_length=11, blank=False, null=False)
    email = models.EmailField(blank=False, null=False)

    marital_status = models.CharField(choices=Marital_Status, max_length=8, blank=False, null=True, default='Single')
    parents = models.CharField(max_length=40, blank=True, null=True)
    parents_contact = models.CharField(max_length=11, blank=False, null=False)

    islamic_knowledge = models.CharField(choices=IslamicKnowledge, max_length=12, blank=False, null=False, default='None')
    number_of_sura_memorized = models.PositiveIntegerField(blank=False, null=True)
    have_you_servered_in_any_islamic_organization = models.CharField(choices=serve_in_organization, max_length=4, blank=False, null=False, default='No')

    organization_1 = models.CharField(max_length = 120, blank=True, null=True)
    organization_address_1 = models.CharField(max_length = 120, blank=True, null=True)
    organization_2 = models.CharField(max_length = 120, blank=True, null=True)
    organization_address_2 = models.CharField(max_length = 120, blank=True, null=True)
    organization_3 = models.CharField(max_length = 120, blank=True, null=True)
    organization_address_3 = models.CharField(max_length = 120, blank=True, null=True)

    position_held_1 = models.CharField(max_length=25, blank=True, null=True)
    position_held_2 = models.CharField(max_length=25, blank=True, null=True)
    position_held_3 = models.CharField(max_length=25, blank=True, null=True)

    
    def get_absolute_url(self):
        return reverse_lazy('register_done')

    def __str__(self):
        return self.surname + ', ' + self.other_name