from django.db import models

# Create your models here.
class Library(models.Model):
    book_id = models.IntegerField()
    book_name = models.CharField(max_length=120)

    def __str__(self):
        return self.book_name

class School(models.Model):
    rollnumber = models.IntegerField()
    std_name = models.CharField(max_length=120)
    std_class = models.CharField(max_length=120)
    joining_date = models.DateField()
    lib = models.ForeignKey(Library,on_delete=models.CASCADE)

    def __str__(self):
        return self.std_name




