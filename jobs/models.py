from django.db import models

# Create your models here.
class Contract(models.Model):
    contract_title = models.CharField(max_length=100, primary_key=True)
    contract_description = models.CharField(max_length=250)
    contract_location = models.CharField(max_length=100)
    contract_salary = models.IntegerField()
    contract_recruiter = models.CharField(max_length=250)
    recruiter_email = models.EmailField()
    recruiter_telephone = models.CharField(max_length=11)
    featured_contract = models.BooleanField(default=False)
    # contract_created_by = 

    def __str__(self):
        return self.contract_title
