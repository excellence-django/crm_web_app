from django.db import models

# Create your models here.
class Student(models.Model):
    rollno=models.CharField(max_length=30,primary_key=True)
    name=models.CharField(max_length=30)
    profile_pic=models.ImageField(upload_to="profilepics",null=True)
    address=models.CharField(max_length=30)
    mobile=models.IntegerField()
    email=models.EmailField(max_length=30,unique=True)
class  Course(models.Model):
    couse_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    details = models.CharField(max_length=100)
class  Enroll(models.Model):
    e_id = models.AutoField(primary_key=True)
    rollno = models.ForeignKey(Student, on_delete=models.CASCADE)

    couse_id= models.ForeignKey(Course, on_delete=models.CASCADE,default=10)


    fees = models.IntegerField(default=0)
    details = models.CharField(max_length=100)
    status = models.CharField(max_length=100,default="Not paid")



