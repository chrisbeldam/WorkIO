import datetime
from django.db import models
from django.utils.translation import gettext as _
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Contract(models.Model):
    contract_id = models.BigAutoField(primary_key=True)
    contract_title = models.CharField(max_length=100)
    contract_description = models.CharField(max_length=250)
    contract_location = models.CharField(max_length=100)
    contract_monthly_salary = models.IntegerField()
    contract_recruiter = models.CharField(max_length=250)
    recruiter_email = models.EmailField()
    recruiter_telephone = models.CharField(max_length=11)
    featured_contract = models.BooleanField(default=False)
    featured_expiry_date = models.DateField(default=datetime.date.today)
    date_created = models.DateField(_("Contract Start Date"), default=datetime.date.today) #This allows for the internationalisation of the date field #
    contract_expiry_date = models.DateField(_("Contract Expiry Date"), default=datetime.date.today)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=True) # Links the user to the role

    def __str__(self):
        return self.contract_title

    def get_absolute_url(self):
        return reverse('contract-detail', kwargs={'pk': self.pk})
