from django.db import models
from login import models as login_model

# Create your models here.
class ECGData(models.Model):
    client_name = models.ForeignKey(to=login_model.User,on_delete=models.CASCADE,to_field='name')
    time_passed = models.TextField()
    ecg = models.TextField()


    def __str__(self):
        return [self.client_name,self.ecg]
