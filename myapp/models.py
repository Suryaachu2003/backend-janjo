
from django.db import models

class student(models.Model):
    datas=[('M','Male'),('F','Female'),('O','Other')]
    name=models.CharField(max_length=50)
    age=models.IntegerField()
    email=models.EmailField()
    gender=models.CharField(max_length=1,choices=datas,null=True)
    file=models.FileField(blank=False, upload_to="pdffile",null=True)
    
    
    class Meta:
        verbose_name_plural="student"
    
    def __str__(self):
        return self.name
class teacher(models.Model):
     datas=[('M','Male'),('F','Female'),('O','Other')]
     sub=[('Maths','Maths'),('Science','Science'),('Social','Social')]
     name=models.CharField(max_length=50)
     subject=models.CharField(max_length=50,choices=sub,null=True)
     gender=models.CharField(max_length=1,choices=datas,null=True)
        
     class Meta:
        verbose_name_plural="teacher"
        
     def __str__(self):
        return self.name
class schoolmanagement(models.Model):
    name=models.CharField(max_length=50)
    address=models.TextField()
    student=models.ManyToManyField(student)
    teacher=models.ManyToManyField(teacher)

    class Meta:
        verbose_name_plural="schoolmanagement"

    def __str__(self):
        return self.name

class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    cover_letter = models.TextField()
    resume = models.FileField(upload_to='resumes/')

# Create your models here.
