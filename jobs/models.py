from django.db import models
import datetime
from django.utils.translation import gettext as _
from django.contrib.auth.models import User

# Create your models here.
class Contract(models.Model):
    contract_title = models.CharField(max_length=100, primary_key=True)
    contract_description = models.CharField(max_length=250)
    contract_location = models.CharField(max_length=100)
    contract_monthly_salary = models.IntegerField()
    contract_recruiter = models.CharField(max_length=250)
    recruiter_email = models.EmailField()
    recruiter_telephone = models.CharField(max_length=11)
    featured_contract = models.BooleanField(default=False)
    date_created = models.DateField(_("Contract Start Date"), default=datetime.date.today) #This allows for the internationalisation of the date field#
    contract_expiry_date = models.DateField(_("Contract Expiry Date"), default=datetime.date.today)
    contract_created_by = models.ForeignKey(User, on_delete=models.CASCADE, default=True) ## Links the user to the role

    class Meta:
        pass

    def __str__(self):
        return self.contract_title + " - " + self.contract_created_by
