from django.db import models
from django.contrib.auth.models import  User
# Create your models here.
class Product(models.Model):

    title = models.CharField(max_length=244)
    pub_date = models.DateTimeField()
    votes_total = models.IntegerField(default=0)
    body = models.TextField()
    url = models.TextField()
    icons = models.ImageField(upload_to='uploads')
    image = models.ImageField(upload_to='uploads')
    hunter = models.ForeignKey(User, on_delete=models.CASCADE  )

    def summary(self):
        return self.body[0:79]

    def pub_date_pretty(self):
        return self.pub_date.strftime("%d %m %Y")

    def __str__(self):
        return self.title

