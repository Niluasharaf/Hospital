from django.db import models

# Create your models here.

class Departments(models.Model):
    spec_name=models.CharField(max_length=100)
    spec_description=models.TextField()

    def __str__(self):
        return self.spec_name


class Doctors(models.Model):
    doc_name=models.CharField(max_length=100)
    doc_spec=models.CharField(max_length=100)
    spec_name=models.ForeignKey(Departments,on_delete=models.CASCADE)
    doc_image=models.ImageField(upload_to="images")

    def __str__(self):
        return self.doc_name + '- (' + self. doc_spec +')'


class Booking(models.Model):
    p_name=models.CharField(max_length=100)
    p_phone=models.CharField(max_length=100)
    p_email=models.EmailField(max_length=100)
    doc_name=models.ForeignKey(Doctors,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)


class Callback(models.Model):
    c_lname=models.CharField(max_length=100)
    c_fname=models.CharField(max_length=100)
    c_email=models.EmailField(max_length=100)
    c_phone=models.CharField(max_length=100)
   


