from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.
class qulificationRfeild(models.Model):
    Qulification = models.CharField(max_length=50)
    details=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.Qulification
    
class Branch(models.Model):
    qualification = models.ForeignKey(qulificationRfeild, on_delete=models.CASCADE)
    branch_name = models.CharField(max_length=50)
    duriations=models.CharField(max_length=500,default="")
    details=models.CharField(max_length=500,default="")

    def __str__(self):
        return self.branch_name
    
class CourseDetails(models.Model):
    branch_name = models.ForeignKey(Branch, on_delete=models.CASCADE)
    course = models.CharField(max_length=50)
    description = RichTextField()
    

    def __str__(self):
        return self.course
