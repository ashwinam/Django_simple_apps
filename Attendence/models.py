from django.db import models
from django.db.models.fields import URLField

# Create your models here.
class Student(models.Model):
    st_id = models.IntegerField()
    st_name = models.CharField(max_length=100)
    st_mail = models.EmailField(max_length=100)
    st_class = models.CharField(max_length=100)

    def __str__(self):
        return str(self.st_id)

# lets creat a DB for student for recording and taking a attendence

class MasterData(models.Model):
    class Meta:
        unique_together = (('st_id','subject'),)
    st_id = models.IntegerField()
    st_name = models.CharField(max_length=100)
    st_mail = models.EmailField(max_length=100)
    subject = models.CharField(max_length=100)

    def __str__(self):
        return str(self.st_id)

#  Mark Attendence Objects access the masterdata using 'ID' and MasterData object access the Mark_Attendence table using 'related_name'
class Mark_Attendence(models.Model):
    class Meta:
        unique_together = (('ID','date1'),('date1','ip_address'))
    ID = models.ForeignKey('MasterData', related_name='S_Id', on_delete=models.CASCADE)
    subject_name = models.CharField(max_length=100)
    time1 = models.IntegerField(null=False)
    ip_address = models.CharField(max_length=100, null=False)
    date1 = models.CharField(max_length=100, null=False)
    platform = models.CharField(max_length=200, null=False)

    def __str__(self):
        return str(self.ID)